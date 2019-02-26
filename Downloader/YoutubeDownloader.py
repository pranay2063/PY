
# 20 october 2015

# script for youtube downloader
# this code does not work for all videos ,eg, VEVO,T-SERIES (restricted background play)

# https://docs.python.org/3/library/urllib.parse.html
# use urllib2.urlopen() in python2 
# use urllib.urlopen()  in python3 and python2
# add ,end="" to print argument in python3 so as not to change line with print

import sys
import urllib2,urlparse

link  = sys.argv[1]
# The object sys.argv is just a list containing everything from the command line
# sys.argv[0] is the name of the script

resp  = urllib2.urlopen("https://www.youtube.com/get_video_info?video_id="+link)
data  = resp.read()
info  = urlparse.parse_qs(data)
title = info['title'][0]
fname = title + ".mp4"
stream_map = info['url_encoded_fmt_stream_map'][0]
v_info = stream_map.split(",")

for video in v_info:
	
	item = urlparse.parse_qs(video)
	url  = item['url'][0]
	#print(url)
	resp = urllib2.urlopen(url)
	length = int(resp.headers['Content-Length'])
	my_file = open("/home/pranay/Videos/" + fname,"w+")
	done = 0
	buff = resp.read(1024)

	while buff:
		my_file.write(buff)
		done += 1024
		percent = done * 100.0 / length
		#print("\r" + str(percent) + "%",end="")     (python3)
		#sys.stdout.write("\r" + str(percent) + "%") (python2)
		print "\r" + str(percent) + "%",             
		buff = resp.read(1024)
	
	break
	
 


