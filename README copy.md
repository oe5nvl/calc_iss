# calc_iss
Calculates the position of ISS for a given observer location.

v0.2: new Doppler calculation methode @skyfield: https://rhodesmill.org/skyfield/earth-satellites.html

Fist Version calc_iss.py
* loads all Satellites from celestrak.com

New in version: calc_iss_v2.py
* loads only one satellite 
* load by catalog nr
* reload TLE Date if older then 7 days
* change load.tle (obsolte ?) do load.tle_file

# Install
```
git clone https://github.com/oe5nvl/calc_iss.git

Do not forget to update the TLE-data. Simply delete stations.txt and restart the program
```
# Start calculation with:
```
python3 ./calc_iss.py
```
# Prerequisite:

Install skyfiled library (https://rhodesmill.org/skyfield/)
```
pip3 install skyfield

```
# Files:
```
calc_iss.py.py   - main program
```

# TLE files are automatically downloaded by Skyfield:
```
stations.txt
```

OE5NVL, OE5RNL