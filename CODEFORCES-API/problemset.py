
# problemset with statistics
# problems can be filtered by tags
# Author : Pranay Ranjan

import sys
from urllib import urlopen
from json import load

param = sys.argv[1]  # argv[0] is the name of the file itself

if param=="none":
	response = urlopen("http://codeforces.com/api/problemset.problems?tags=")
else :
	response = urlopen("http://codeforces.com/api/problemset.problems?tags="+param)

json_obj = load(response)

i = 0
obj2 = json_obj['result']['problemStatistics']

for obj in json_obj['result']['problems']:
	print obj['name']+" ("+str(obj['contestId'])+obj['index']+") , Solved : "+str(obj2[i]['solvedCount'])
	i += 1


