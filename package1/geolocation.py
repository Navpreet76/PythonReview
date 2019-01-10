import re
import sys
import urllib2
from bundlebuilder import usage
from pip._vendor.urllib3.packages.ssl_match_hostname._implementation import ipaddress
from pip._internal.index import _get_html_page
from StdSuites.Text_Suite import paragraph

usage="Run the script:./geolocation.py IPAddress"

if len(sys.argv)!=2:
    print(usage)
    sys.exit(0)
if len(sys.argv)>1:
    ipaddr=sys.argv[1]
geody="http://www.geody.com/geoip.php?ip="+ ipaddr
html_page=urllib2.urlopen(geody).read()
soup = html_page
#filter paragraph containing geolocation info
paragraph = soup('p')[3]

#Remove html tags using regex
geo_txt = re.sub(r'<.*?>', '', str(paragraph))
print geo_txt[32:].strip()
