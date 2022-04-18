"""
In this below topic we will talk about dropdown
a) static - the dropdown values will remain the same and will not chnage
b) dynamic - the values in the dropdown are populated as we type 
Example - "City" downdown in any booking website
"""

from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

# when selecting the downdown user needs to pass the locator for the dropdown
# "Select" package can be only be used where dropdown has a tag of "select"
dropdownobj = Select(calldriver.find_element(by=By.ID,value='exampleFormControlSelect1'))

# selecting in the dropdown on the basis of visible text
dropdownobj.select_by_visible_text('Female')
time.sleep(5)

# selecting on the basis of index
dropdownobj.select_by_index(0)
time.sleep(5)

# selecting on the basis of value
# value can only be used if the drop has an value tag. please make user verifies if there is any tab with values for the dropdown 
# dropdownobj.deselect_by_value

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
