
# python program to show the rating changes of a user in the contests he/she participated on codeforces
# Author : Pranay Ranjan

import sys
from urllib import urlopen
from json import load

param = sys.argv[1] # argv[0] is the name of the file itself
response = urlopen(" http://codeforces.com/api/user.rating?handle="+param)
json_obj = load(response)

for obj in json_obj['result']:
	print("ContestId : "+str(obj['contestId']))
	print("Contest Name: "+obj['contestName'])
	print("Rank : "+str(obj['rank']))
	print("Old Rating : "+str(obj['oldRating']))
	print("New Rating : "+str(obj['newRating']))
	print("")










