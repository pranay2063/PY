
# python program to print last 10 submissions' details of a user on Codeforces
# Author : Pranay Ranjan

import sys
from urllib import urlopen
from json import load

param = sys.argv[1] # argv[0] is the name of the file itself
response = urlopen("http://codeforces.com/api/user.status?handle="+param+"&from=1&count=10")
json_obj = load(response)

for obj in json_obj['result']:
	print("submission Id : "+str(obj['id']))
	print("Contest Id : "+str(obj['contestId']))
	print("Created    : "+str(obj['creationTimeSeconds'])+" seconds ago")
	print("Problem Id : "+str(obj['problem']['contestId'])+" "+obj['problem']['index'])
	print("Problem Name : "+obj['problem']['name'])
	print "Tags :",
	for tag in obj['problem']['tags']:
		print tag,
	print("")
	print("Language : "+obj['programmingLanguage'])
	print("Verdict  : "+obj['verdict'])
	print("Passed test : "+str(obj['passedTestCount']))
	print("Execution time : "+str(obj['timeConsumedMillis'])+" ms")
	print("Memory : "+str(obj['memoryConsumedBytes']/(1024*1024.0))+" MB")
	print("")







