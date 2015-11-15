
# Python script to show all contests' details
# Author : Pranay Ranjan

from urllib import urlopen
from json import load

response = urlopen("http://codeforces.com/api/contest.list?gym=true")
json_obj = load(response)

for obj in json_obj['result']:
	print("\nContest ID : "+str(obj['id']))
	print("Name : "+obj['name'])
	print("Type : "+str(obj['type']))
	print("Phase : "+str(obj['phase']))
	#print("Start : "+str(obj['startTimeSeconds']))
	print("Duration : "+str(obj['durationSeconds']))

