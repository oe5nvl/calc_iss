

################################################################
# Deep Space Set_Oberating_Mode
# Groundstation software v2
# (c) oe5nvl, oe5rnl
#
# https://rhodesmill.org/skyfield/earth-satellites.html
# https://rhodesmill.org/skyfield/examples.html
#

import math
from skyfield.api import Star, Topos, Loader
from skyfield.api import load
import time, datetime
from datetime import datetime

dss_qth    = Topos("48.3314536111111N","13.9797030555556E")
sat_qrg    = 437.550
catalog_nr = 25544
#sat_name   = "ISS (ZARYA)"

# load tle data for the iss station
stations_url = 'https://celestrak.com/satcat/tle.php?CATNR={}'.format(catalog_nr)
filename = 'tle-CATNR-{}.txt'.format(catalog_nr)
satellites = load.tle_file(stations_url, filename=filename)

by_number = {sat.model.satnum: sat for sat in satellites}
satellite = by_number[catalog_nr]

ts_ = load.timescale()
t   = ts_.now()  # Time
#t   = ts_.utc(2022, 7, 1, 11, 18, 7)

days = t - satellite.epoch
print()    
print("****************************************************")
print("epoch.utc_jpl     "+str(satellite.epoch.utc_jpl()))
print('TLE Data:         {:.3f} days away from epoch'.format(days))
print()
if abs(days) > 7:
    satellites = load.tle_file(stations_url, filename=filename, reload=True)

# calculate sat data
relative_postion                  = satellite - dss_qth
topocentric                       = relative_postion.at(t)
alt, az, distance                 = topocentric.altaz()
_, _, the_range, _, _, range_rate = topocentric.frame_latlon_and_rates(dss_qth)  # new calculation methode @skyfield
doppler                           = (1 + range_rate.km_per_s * 1e3 / 299792458)  * sat_qrg - sat_qrg

print("Azimut:           "+str(az.degrees))              # az
print("Elevation         "+str(alt.degrees))             # el
print()
print("Time_JD:          "+str(t))                       # observation time 
print("Time_UTC:         "+str(t.utc_datetime()))        # observation time 
print("Name:             "+str(satellite.name))          # Sat name   
print("QRG:              "+str(sat_qrg))                 # QRG
print("Doppler:          "+str(doppler))                 # dopper shift
print("Rx_QRG:           "+str(sat_qrg+doppler))         # Rx QRG
print("Distance.km:      "+str(the_range.km))            # [km]      distance
print("Range_speed.kms:  "+str(range_rate.km_per_s))     # [km/s]    delot
print("Distance.au:      "+str(distance.au))             # [AU]      distance in AU
print("Distance.lm:      "+str(distance.km / 1.799e+7))  # [l_min]   distance in light Minutes
print("Distance.ly:      "+str(distance.km / 9.461e+12)) # [LY]      distance in distance in light Years 
print("****************************************************")
print()
