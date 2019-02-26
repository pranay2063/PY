
import os
import re
import sys
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/count", methods=['POST'])
def count():
	
	#read data posted at UI
	_txt = request.form['txt']
	#lst = _txt.split(' ')
	lst = re.findall(r"[\w']+", _txt)	
	cnt = len(lst)

	return 'No of words in the text is '+str(cnt)

if __name__ == '__main__':
	#app.run()
	port = int(os.environ.get("PORT", 5000))
    	app.run(host='0.0.0.0', port=port)
