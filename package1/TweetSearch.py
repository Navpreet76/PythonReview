#Importing the modules
import urllib2
import json

screen_name = "@KingJames"

url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=" + screen_name

data = json.load(urllib2.urlopen(url))

print len(data), "tweets"

for tweet in data:
    print tweet['text']
    
#This is not working properly, figure out why we are getting all these violations