"""
As a part of the we are going to learn two things
a) use actions class for doing double click mouse 
b) we can right click using the context 
"""
from codecs import BOM_LE
import time
from unittest.loader import VALID_MODULE_NAME
from xmlrpc.client import Boolean
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


callservice = ChromeService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")
driver = webdriver.Chrome(service=callservice)

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
# here we are going to use action class

action = ActionChains(driver)
doubleclick=driver.find_element(by=By.XPATH,value="//input[@id='double-click']")

#context click
action.move_to_element(doubleclick).context_click().perform()

#double click
action.move_to_element(doubleclick).double_click().perform()
time.sleep(2)

# handing popup box
popuphandle = driver.switch_to.alert
time.sleep(2)
popuptext = popuphandle.text
print(popuptext)
assert "You double clicked me" in popuptext

popuphandle.accept()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

"""
assert driver.find_element(by=By.ID,value="displayed-text").is_displayed()
driver.find_element(by=By.ID,value='hide-textbox').click()
assert not driver.find_element(by=By.ID,value="displayed-text").is_displayed()
"""

# hidden textbox
textbox = driver.find_element(by=By.ID,value="displayed-text").is_displayed()
print (textbox)
if textbox:
    time.sleep(5)
    driver.find_element(by=By.ID,value='hide-textbox').click()
    time.sleep(2)
else:
    print("The box does not exist")

driver.close()