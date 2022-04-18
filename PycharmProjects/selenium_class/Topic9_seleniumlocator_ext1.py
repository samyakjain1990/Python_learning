"""
RelativeXpath - This path is generated using the exact element searching in the whole page
AbsoluteXpath - This path is generated from the top of the page using tags

Always it is better to use relative becuase absolute path can change after adding one images/extra frame/extra buttons but relative path will not change
"""

from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

driverservice = FirefoxService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/geckodriver")
loaddriver = webdriver.Firefox(service=driverservice)

loaddriver.get("https://login.salesforce.com")

loaddriver.find_element(by=By.LINK_TEXT,value="Forgot Your Password?").click()
time.sleep(2)

# This tagname with text only works in case of "a" (links)
loaddriver.find_element(by=By.XPATH,value="//a[text()='Need Help Logging In?']").click()
time.sleep(2)

loaddriver.back()
time.sleep(2)

# Need to understand why it does not take the xpath when we take an tag "input" which is a button ???
loaddriver.find_element(by=By.XPATH,value="//input[@name='cancel']").click()
time.sleep(2)

loaddriver.find_element(by=By.LINK_TEXT,value="Try for Free").click()
time.sleep(2)

# using parent child traverse tag machanism
# for css we need to give space "div[id='signup'] a"
# for xpath we need to give "/" instead of space "div[id='signup']/a"
loaddriver.find_element(by=By.XPATH,value="//div[contains(@class,'firstName textFieldInput section')]/div[1]/input").send_keys("Anthony")
time.sleep(2)

loaddriver.find_element(by=By.CSS_SELECTOR,value="div[class*='lastName textFieldInput section'] div input").send_keys("Nomad")
time.sleep(2)

loaddriver.close()