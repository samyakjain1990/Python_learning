"""
Verify if your csslocator/xpath is unique or not before using it

CSS Locator
Steps:
a) Open Console tab using inspect which is present in every browser
b) type $(input[name='email']) - do not copy paste 
c) expand $(input[name='email'])  
d) verify you see only one element higlighted after hovering over "input 0/1"

xpath
Steps:
a) Open Console tab using inspect which is present in every browser
b) type $x(//input[@type='password'])

you can use cropath as a plugin for checking the xpath

"""


from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

callservice = FirefoxService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/geckodriver")
calldriver = webdriver.Firefox(service=callservice)

calldriver.get("https://rahulshettyacademy.com/angularpractice") 

calldriver.find_element(by=By.NAME,value="name").send_keys("Anthony")
time.sleep(2)

# Syntax for CSS 
# tagname[attribute=value]
# "input[name='email']"
calldriver.find_element(by=By.CSS_SELECTOR,value="input[name='email']").send_keys("mynameisanthony@gmail.com")
time.sleep(2)

calldriver.find_element(by=By.ID,value="exampleInputPassword1").send_keys("thisisjustpassword")
time.sleep(2)

calldriver.find_element(by=By.CSS_SELECTOR,value="input[type='checkbox']").click()
time.sleep(2)

# Syntax for xpath
# //tagname[attribute=value]
# "//input[@name='email']"
calldriver.find_element(by=By.XPATH,value="//input[@value='Submit']").click()
time.sleep(2)

# Pulling the submit text after submitting 
# if you suspect of having more than 1 element with same class name then you can use 
# http://makeseleniumeasy.com/2020/11/11/wildcard-characters-in-xpath-selenium-webdriver/
formtext= calldriver.find_element(by=By.CLASS_NAME,value="alert-success").text
print(formtext)

print(calldriver.find_element(by=By.CSS_SELECTOR,value="div[class*='alert-success']").text)

print(calldriver.find_element(by=By.XPATH,value="//div[contains(@class,'alert-success')]").text)

calldriver.close()
