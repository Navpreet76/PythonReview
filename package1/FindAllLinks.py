import urllib2
import re

#connect to a URL
website=urllib2.urlopen("https://www.amazon.com")

#read html code
html = website.read()

links=re.findall('"((http|ftp)s?://.*?)"',html)
print links


#This is giving errors as well, figure out what is going on here