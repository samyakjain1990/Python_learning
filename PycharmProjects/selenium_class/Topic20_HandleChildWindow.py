"""
# now the new window has opened up we need to the below steps to naviagte to the new window
# a) Get the control over the browser
# b) switch to another window using it
"""

import time
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driverservice = FirefoxService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/geckodriver")
drivercall = webdriver.Firefox(service=driverservice)

drivercall.get("https://the-internet.herokuapp.com/windows")
drivercall.find_element(by=By.LINK_TEXT,value="Click Here").click()

# usually the parent has value 0 and the next child windows start from 1
# ("Parentid","childid")
getchildhandle =drivercall.window_handles[1]
print(getchildhandle)

time.sleep(5)

drivercall.switch_to.window(getchildhandle)
print(drivercall.find_element(By.TAG_NAME,value="h3").text)

getparenthandle = drivercall.window_handles[0]

drivercall.switch_to.window(getparenthandle)
print(drivercall.find_element(By.TAG_NAME,value="h3").text)

drivercall.close()