# calc_iss
Calculates observer data for the ISS for a given observer location.

```
Hallo
```

Features:

* Loads the ISS TLE data or for other satellte by CATNR 
* Reload TLE Date if older then 7 days
* Display Azimut, Elivation, doppler shift and other Data
* Display predict data for the next n days 
* Delete File tle-CATNR-2544.txt for reload TLE data now and restart the program.

# Install

```
git clone https://github.com/oe5nvl/calc_iss.git
```

# Prerequisite:

```
Install skyfiled library (https://rhodesmill.org/skyfield/)

pip3 install skyfield

Install timezone support

pip3 install pytz
```

# Start calculation with:

```
python3 ./calc_iss.py
```


# Files:
```
calc_iss.py   - main program
```

# TLE files are automatically downloaded by Skyfield:
```
tle-CATNR-25544.txt
```

OE5NVL, OE5RNL
