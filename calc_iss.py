################################################################
# Deep Space Set_Oberating_Mode
# Groundstation software
# (c) oe5nvl, oe5rnl
#
# https://rhodesmill.org/skyfield/earth-satellites.html
#

import math
from skyfield.api import Star, Topos, Loader
from skyfield.api import load
import time, datetime
from datetime import datetime

sat_qrg                           = 145.8
sat_name                          = "ISS (ZARYA)"

satellites                        = load.tle("http://celestrak.com/NORAD/elements/stations.txt") # get TLE
ts_                               = load.timescale()
t                                 = ts_.now()                                                    # Time

dss_qth                           = Topos("48.3314536111111N","13.9797030555556E")
relative_postion                  = satellites[sat_name] - dss_qth
topocentric                       = relative_postion.at(t)
alt, az, distance                 = topocentric.altaz()
_, _, the_range, _, _, range_rate = topocentric.frame_latlon_and_rates(dss_qth)  # new calculation methode @skyfield
doppler                           = (1 + range_rate.km_per_s * 1e3 / 299792458)  * sat_qrg - sat_qrg

print()    
print("****************************************************")
print("Time_JD:          "+str(t))                       # observation time 
print("Time_UTC:         "+str(t.utc_datetime()))        # observation time 
print("Name:             "+str(sat_name))                # Sat name   
print("QRG:              "+str(sat_qrg))                 # QRG
print("Doppler:          "+str(doppler))                 # dopper shift
print("Rx_QRG:           "+str(sat_qrg+doppler))         # Rx QRG
print("Az:               "+str(az.degrees))              # az
print("El:               "+str(alt.degrees))             # el
print("Distance.km:      "+str(the_range.km))            # [km]      distance
print("Range_speed.kms:  "+str(range_rate.km_per_s))     # [km/s]    delot
print("Distance.au:      "+str(distance.au))             # [AU]      distance in AU
print("Distance.lm:      "+str(distance.km / 1.799e+7))  # [l_min]   distance in light Minutes
print("Distance.ly:      "+str(distance.km / 9.461e+12)) # [LY]      distance in distance in light Years 
print("****************************************************")
print()




#
# range_velocity     = topocentric.velocity.km_per_s
# range_speed        = math.sqrt(range_velocity[0]**2 + range_velocity[1]**2+range_velocity[2]**2)
# doppler            = (1 + range_speed * 1e3 / 299792458)  * sat_qrg - sat_qrg