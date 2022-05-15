# JS DOM can access any element on webpage just like how selenium does
# selenium has a method via which we can run javascript code in it

from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

callservice = FirefoxService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/geckodriver")
calldriver = webdriver.Firefox(service=callservice)

calldriver.get("https://rahulshettyacademy.com/angularpractice") 
calldriver.find_element(by=By.NAME,value="name").send_keys("Helloz")

# now suppose after inputting above text you want to retrieve the text whatever we wrote in the textbox
#calldriver.find_element(by=By.NAME,value="name").text
# code written above will not work in retriveing the text because "text" method can only work on the data of inital DOM not on the data added using selenium


# Getting data from the textbox
calldriver.find_element(by=By.NAME,value="name").get_attribute("value")

# finding data present in the textbox using javascript 
print(calldriver.execute_script('return document.getElementsByName("name")[0].value'))

# here in line 28 argument is decided on the basis of the number of arguments passed
# Ex : ("argument[].click();",abc,xyz,wer) 
# now if you want to click "xyz" the argument value will be argument[1]
shopbutton = calldriver.find_element(by=By.CSS_SELECTOR,value="a[href*='shop']")
calldriver.execute_script("arguments[0].click();",shopbutton)

time.sleep(5)
calldriver.back()

# selenium does not have not any method for scrolling in a page instead we can use the below method from java script
# in this case the 0 means top of the window and document.body.scrollHeight finds the max height to which we can scroll
# user can also give 0,500 or 500,0 (0 means top and 500 means a height in the doc)
calldriver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

#calldriver.close()
