from os import X_OK
from selenium import webdriver
import time


web = webdriver.Safari()
web.get('')

time.sleep(2)

LastName = ""
last = web.find_element_by_xpath('')
last.send_keys(LastName)

FirstName = ""
first = web.find_element_by_xpath('')
first.send_keys(FirstName)


Submit = web.find_element_by_xpath('')
Submit.click()

time.sleep(5)

list = []
for x in range(0, len(list), 5):
    Submit1 = web.find_element_by_xpath('')
    Submit1.click()
    
    PageUrl = str(list[x+1])
    url = web.find_element_by_xpath('')
    url.send_keys(PageUrl)

    Pagetitle = str(list[x])
    title = web.find_element_by_xpath('')
    title.send_keys(Pagetitle)
    
    imageUrl = str(list[x+4])
    image1 = web.find_element_by_xpath('')
    image1.send_keys(imageUrl)

    description = str(list[x+2] + "," + list[x+3]) 
    describe = web.find_element_by_xpath('')
    describe.send_keys(description)

    tags = "#" + str(list[x])
    insertTag = web.find_element_by_xpath('')
    insertTag.send_keys(tags)
    
    time.sleep(3)

    Submit2 = web.find_element_by_xpath('')
    Submit2.click()
    
    time.sleep(2)
