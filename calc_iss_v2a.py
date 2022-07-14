

################################################################
# Deep Space Set_Oberating_Mode
# Groundstation software v2
# (c) oe5nvl, oe5rnl 
#
# https://rhodesmill.org/skyfield/earth-satellites.html
# https://rhodesmill.org/skyfield/examples.html
#
# https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle
#

import datetime as dt
import skyfield.api as sf
from skyfield import VERSION
from pytz import timezone


def getTLE(t0, catalog_nr):

        stations_url = 'https://celestrak.com/satcat/tle.php?CATNR={}'.format(catalog_nr)
        filename     = 'tle-CATNR-{}.txt'.format(catalog_nr)
        satellites   = sf.load.tle_file(stations_url, filename=filename)
        by_number    = {sat.model.satnum: sat for sat in satellites}
        satellite    = by_number[catalog_nr]

        days         = t0 - satellite.epoch

        if abs(days) > 7:
            satellites = sf.load.tle_file(stations_url, filename=filename, reload=True)
            by_number  = {sat.model.satnum: sat for sat in satellites}
            satellite  = by_number[catalog_nr]

        return days, satellite

def getPredict(t0, days, observer_qth, satellite):
  
    zone = timezone('Europe/Vienna')
    now = zone.localize(dt.datetime.now())
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    next_midnight = midnight + dt.timedelta(days=days)
    t1 = ts.from_datetime(next_midnight)

    t, events = satellite.find_events(observer_qth, t0, t1, altitude_degrees=above) 

    pre = []
    for ti, event in zip(t, events):
        name = ('rise above '+str(above), 'culminate', 'set below '+str(above))[event]
        pre.append(str(ti.astimezone(zone))+' '+ name)
        # print(ti.utc_strftime('%Y %b %d %H:%M:%S'), name)

    return pre

if __name__ == "__main__":

    lat             = +48.301  # obersver location lat
    lon             = +14.3    # obersver location lon
    catalog_nr      = 25544    # ISS
    sat_qrg         = 145.800  # ham radio frequency
    above           = 10.0     # satellite must be degrees over horizon ?

    observer_qth    = sf.wgs84.latlon(lat,lon)
    ts              = sf.load.timescale()
    t0              = ts.now()  # Time utc !!!
    days, satellite = getTLE(t0, catalog_nr) 

    # calculate satellite data
    relative_postion                  = satellite - observer_qth
    topocentric                       = relative_postion.at(t0)
    alt, az, distance                 = topocentric.altaz()
    _, _, the_range, _, _, range_rate = topocentric.frame_latlon_and_rates(observer_qth)  # new calculation methode @skyfield
    doppler                           = (1 + range_rate.km_per_s * 1e3 / 299792458)  * sat_qrg - sat_qrg

    print()    
    print("****************************************************")
    print("skyfield.VERSION:        "+str(VERSION))
    print("epoch.utc_jpl            "+str(satellite.epoch.utc_jpl()))
    print('TLE Data:                {:.3f} days away from epoch'.format(days))
    print("Satellite:               {0:} degrees over horizon".format(above))
    print("Azimut:                  {0:.3f}".format(az.degrees))    # az
    print("Elevation                {0:.3f}".format(alt.degrees))   # el
    print()
    print("Time_JD:                 "+str(t0))                      # observation time 
    print("Time_UTC:                "+str(t0.utc_datetime()))       # observation time 
    print("Name:                    "+str(satellite.name))          # Sat name   
    print("QRG:                     "+str(sat_qrg))                 # QRG
    print("Doppler:                 "+str(doppler))                 # dopper shift
    print("Rx_QRG:                  "+str(sat_qrg+doppler))         # Rx QRG
    print("Distance.km:             "+str(the_range.km))            # [km]      distance
    print("Range_speed.kms:         "+str(range_rate.km_per_s))     # [km/s]    delot
    print("Distance.au:             "+str(distance.au))             # [AU]      distance in AU
    print("Distance.lm:             "+str(distance.km / 1.799e+7))  # [l_min]   distance in light Minutes
    print("Distance.ly:             "+str(distance.km / 9.461e+12)) # [LY]      distance in distance in light Years 
    print()

    print("Satellite rises and sets:")
    r = getPredict(t0, 1, observer_qth, satellite)
    for e in r:
        print(e)


    