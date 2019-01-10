#!/usr/bin/env python

#import the modules
import sys
import urllib2
import re
import json



#Ask for movie title
title = raw_input("Please enter a movie title: ")

#Ask for which year
year = raw_input("which year? ")
#Search for spaces in the title string
raw_string = re.compile(r' ')

#Replace spaces with a plus sign
searchstring = raw_string.sub('+', title)

#Print the search string
print searchstring

#The actual query
url = "http://www.imdbapi.com/?t=" + searchstring + "&y="+ year
request = urllib2.Request(url)
response = json.load(urllib2.urlopen(request))
print json.dumps(response, indent=2)
