import urllib
import re

print "We will attempt to open this URL, in order to get IP Address"

url = "http://checkip.dyndns.org"

print url

request = urllib.urlopen(url).read()

theIP = re.findall(r"d{1,3}.d{1,3}.d{1,3}.d{1,3}", request)

print "your IP Address is: ",  theIP