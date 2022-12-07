#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Download data from api


# -----------------------------------
# Load libraries

import urllib
import json

# -----------------------------------
# Variables

__api_a = "https://api.geoapify.com/v1/geocode/search?text="
__api_b = "&apiKey="

# https://myprojects.geoapify.com/
__apikey = "1b91736d5eec459fb3f715d9f0a61e2d"


# -----------------------------------
# Script

def get_coordinates(cities: list):
    for city in cities:

        request = __api_a + city + __api_b + __apikey

        try:
            response = urllib.urlopen(request)
            data = json.loads(response.read())

            properties = data["features"][0]["properties"]

            lat = properties["lat"]
            lon = properties["lon"]

            return city, lat, lon

        except:
            print(">>> error: " + city)

            pass


# -----------------------------------
# Launch scripts

'''

python /Users/giovanni/Dropbox/Activities/0_Personale/_code/python/data-from-api/location-to-coordinates.py


'''
