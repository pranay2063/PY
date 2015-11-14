
# Python script to show problems and winner of any contest in Terminals
# Author : Pranay Ranjan

from urllib import urlopen
from json import load

response = urlopen("http://codeforces.com/api/contest.standings?contestId=374&from=1&count=1&showUnofficial=true")
json_obj = load(response)

if json_obj['status']=="FAILED":
	print("Failed")

print("contest ID : "+str(json_obj['result']['contest']['id'])+"\nName : "+json_obj['result']['contest']['name']) 

for obj in json_obj['result']['problems']:

	print("\n"+str(obj['contestId'])+obj['index']+" : "+obj['name'])
	print("Points : "+str(obj['points']))
	print "Tags : ",	
	for tag in obj['tags']:	
		print tag,
	print("\n")

for row in json_obj['result']['rows']:
	print "Winner : ",
	for member in row['party']['members']:
		print member['handle']+" ",
	print(" ")
	print("Participation : "+row['party']['participantType'])
	print("Points : "+str(row['points']))
	print("Hacks  : "+str(row['successfulHackCount']))
	print("penalty : "+str(row['penalty']))


	
