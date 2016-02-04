
# search any element in a html page

from selenium import webdriver

browser = webdriver.Firefox()

type(browser)
browser.get('https://gabrielecirulli.github.io/2048/')

try:
	elem = browser.find_element_by_class_name('game-explanation')
	print('found <%s> element with this class name!' %(elem.tag_name))
except:
	print('no such element')

	
 


