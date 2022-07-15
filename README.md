# calc_iss

This program calculates the iss satelitte position data for a given observer location

Features:

* Loads the ISS TLE data or for other satellte by CATNR 
* Loads the tle data for the satellite if the tle data is older than 7 days
* Displays azimut, elivation, doppler shift and other data
* Displays predicted data for the next n days 
* If you want to force an immediate reload of the data, delete the .txt file

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
Set observer lan/lon in calc_iss.py then start

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

OE5NVL, OE5RNL 7.22
