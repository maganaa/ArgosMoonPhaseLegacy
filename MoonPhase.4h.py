#!/usr/bin/python3

import urllib.request
import json
import emoji

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

#Exception catching as fracillum and curphase don't appear on JSON if closestphase is exact
try:
    fracillum = formatMoonURL['fracillum']
    curphase = formatMoonURL['curphase']
except KeyError:
    curphase = formatMoonURL['closestphase']['phase']
    if curphase == "Full Moon":
        fracillum = "100%"
    elif curphase == "New Moon":
        fracillum = "0%"
    elif curphase == "First Quarter" or curphase == "Last Quarter":
        fracillum = "50%"

#The emojis are inverted to make the highlighted portion of the moon emoji match the illuminated portion of the moon on GNOME
if curphase == "New Moon":
    print(emoji.emojize(":full_moon:"))

elif curphase == "Waxing Crescent":
    print(emoji.emojize(":waning_gibbous_moon:"))

elif curphase == "First Quarter":
    print(emoji.emojize(":last_quarter_moon:"))

elif curphase == "Waxing Gibbous":
    print(emoji.emojize(":waning_crescent_moon:"))

elif curphase == "Full Moon":
    print(emoji.emojize(":new_moon:"))

elif curphase == "Waning Gibbous":
    print(emoji.emojize(":waxing_crescent_moon:"))

elif curphase == "Last Quarter":
    print(emoji.emojize(":first_quarter_moon:"))

elif curphase == "Waning Crescent":
    print(emoji.emojize(":waxing_gibbous_moon:"))

else:
    print("Error")

print("---")
print(curphase)
print(fracillum)
