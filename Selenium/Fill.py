
# filling out and submitting forms
# we need to send key strokes to text fields on a webpage
# first we find <input> or <textarea> element
# then we call send_keys() method

from selenium import webdriver
browser = webdriver.Firefox()

browser.get('https://login.yahoo.com/')

emailElem = browser.find_element_by_id('username')
emailElem.send_keys('abc')
emailElem.submit()


passElem = browser.find_element_by_id('passwd')
passElem.send_keys('123')
passElem.submit()






