
# automate mouse click on a website (or browser)

# open firefox
# get the webElement for <a> element with the text
# simulate clicking that <a> element
# click() method simulates a mouse click on this element

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
link = browser.find_element_by_link_text('Gabriele Cirulli.')
type(link)

link.click() 
