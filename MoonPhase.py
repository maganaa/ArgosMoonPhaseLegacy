#!/usr/bin/python3

import urllib.request, json

#Find User Location
locationURL = 'http://freegeoip.net/json'
openLocationURL = urllib.request.urlopen(locationURL).read()
formatLocationURL = json.loads(openLocationURL)
lat = formatLocationURL['latitude']
lon = formatLocationURL['longitude']

#Moon Phase Finder
moonURL = "http://api.usno.navy.mil/rstt/oneday?date=today&coords=" + str(lat) + "," + str(lon)
openMoonURL = urllib.request.urlopen(moonURL).read()
formatMoonURL = json.loads(openMoonURL)
fracillum = formatMoonURL['fracillum']
curphase = formatMoonURL['curphase']
print("MoonPhase")
print("---")
print(curphase)
