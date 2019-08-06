
import re 
import urllib


def scrapper(start, end, sem):
	url = 'http://dolphintechnologies.in/manit/accessview.php'
	# response = urllib2.urlopen(url)
	# html = response.readlines()

	# file = open('ECE5.txt','a')

	res = {}

	for itr in range(start, end):
		scholarNo = str(itr)
		semester = str(sem)

		data = { "scholar" : scholarNo , "semester" : semester }
		encoded_data = urllib.urlencode(data)
		# filename = 'results.txt'
		# urllib.urlretrieve(url,filename,lambda x,y,z:0,encoded_data)

		# file1 = open(filename,'r')
		# file2 = file1.read()

		content = urllib.urlopen(url, encoded_data)
		html = content.read()		
		# html = str(html)
		# print html
		formatted = re.findall(r'<br />(.*?)<br />', html)

		if not formatted:
			continue
	
		name = re.findall(r'<span class="style3">\s*(.*?)</span>', html) 
		name = name[4]

		# print formatted
		form = []
		for st in formatted:
			if st.startswith('EC') or st.startswith('HUM') or st.startswith('<div align'):
				continue
			else:
				form.append(st)

		# print form

		full_credits = re.findall(r"<br /><div align='center'>(.*?)<br />", html) 

		subjects = form[0:9]
		credits = form[9:18] # credits obtained
		marks = form[18:27]
		grade = form[27:36]

		SGPA = 0
		tcredits = 0 # total of full credits in subjects
		obtained = 0 # total of obtained credits

		# print subjects, credits, marks, grade

		for i in range(0,9):
			SGPA = SGPA + float(full_credits[i])*float(marks[i])	
			tcredits = tcredits + float(full_credits[i])	
			obtained = obtained + float(credits[i])
			# print subjects[i]+' '+credits[i]+' '+marks[i]+' '+grade[i]

		if obtained == 0:
			continue
	
		SGPA = SGPA / tcredits
		SGPA = round(SGPA,2)
		SGPA = format(SGPA,'.2f')

		# file.write(scholarNo+" "+str(SGPA)+" "+name+"\n")
		# print scholarNo+" "+str(SGPA)+" "+name

		# store data in JSON format
		# JSON is a lightweight format of storing data and is easy to transfer across servers
		# JSON is Javascript Object Notation and is not a subset of Javascript language

		res[itr] = [str(SGPA), name]
		print itr
	
	return res
	



