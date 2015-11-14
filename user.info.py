
# Python script to show details of any handle taken as command line input
# Author : Pranay Ranjan

import sys
from urllib import urlopen
from json import load
from pprint import pprint

param = sys.argv[1] # argv[0] is the name of the file itself

response = urlopen("http://codeforces.com/api/user.info?handles="+param)
json_obj = load(response)

for obj in json_obj['result']:	
	print "Handle : "+obj['handle']

	if 'firstName' in obj.keys():
		print "Name : "+obj['firstName']+" ",
		if 'lastName' in obj.keys():
			print obj['lastName'],
		print("")
	if 'country' in obj.keys():
		print "Country/City : "+obj['country']+"/",
		if 'city' in obj.keys():
			print obj['city'],
		print("")	
	if 'organisation' in obj.keys():
		print("Organisation : "+obj['organization'])	

	print "Rating/MaxRating : "+str(obj['rating'])+"/"+str(obj['maxRating'])
	print "Contribution : "+str(obj['contribution'])
	print "Last Online  : "+str(obj['lastOnlineTimeSeconds'])+" seconds ago"
	print "Registered   : "+str(obj['registrationTimeSeconds'])+" seconds ago"
	
	print ""






