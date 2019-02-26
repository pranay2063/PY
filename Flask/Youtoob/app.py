
import sys
import urllib2,urlparse
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/fetch", methods=['POST'])
def fetch():
	
	#read the posted value from UI
	_url = request.form['url']
	resp  = urllib2.urlopen("https://www.youtube.com/get_video_info?video_id="+_url)
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

	return 'Done'
	

if __name__ == '__main__':
	app.run()
  
  
