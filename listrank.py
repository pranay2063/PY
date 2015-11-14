
#Python script to show RankList starting from Rank 1 in Terminal
#Author : Pranay Ranjan

from urllib import urlopen
from json import load

response = urlopen(" http://codeforces.com/api/user.ratedList?activeOnly=")
json_obj = load(response)

for obj in json_obj['result']:
	print("Handle : "+obj['handle'])
	print("Rating : "+str(obj['rating']))
	
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
	
	print("Contribution : "+str(obj['contribution']))	
	print("Rank : "+obj['rank'])
	print("MaxRank : "+obj['maxRank'])
	print("")

print("No. of entries : "+str(len(json_obj['result'])))

	
