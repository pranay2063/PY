

import re
import urllib
import requests 
import os.path
#https://stackoverflow.com/questions/30536946/how-to-install-requests-module-in-python-3-4-version-on-windows

#https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
#https://stackoverflow.com/questions/35842873/is-there-a-way-to-download-a-video-from-a-webpage-with-python
def download_file(url, size):

	local_filename = "C:/Users/I338886/Downloads/ZM/" + url.split('/')[-1]
	completion = 0
	with requests.get(url, stream=True) as r:
		with open(local_filename, 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192):
				if chunk:
					f.write(chunk)
					completion += 8192
					print "\r" + str(completion*100.0/float(size)) + "%",
	print "\n",
	return local_filename					

url = 'http://dl8.heyserver.in/serial/Narcos.Mexico/S01/480p/'
HTMLstring = urllib.urlopen(url).read()
#print HTMLstring

links = []
data = re.findall('href="(.*)"', HTMLstring)
for link in data:
	if not link.endswith('/'):
		links.append(url+link)

for link in links:
	if not os.path.exists("C:/Users/I338886/Downloads/ZM/"+link.split('/')[-1]) :
		attributes = requests.head(link)
		#print attributes.headers['Content-Length']
		print "Download started : " + link
		result = download_file(link,attributes.headers['Content-Length'])
		if result:
			print "Downloaded file : " + link + "\n"
	#myfile = open('C:\Users\I338886\Downloads\ZM'+local_filename,'w+')
	#myfile.write()
