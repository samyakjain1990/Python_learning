"""
Here we are java/java script alerts.
we are only 3 methods here
a) accept
b) dismiss
"""


from subprocess import call
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

callservice = ChromeService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")
calldriver = webdriver.Chrome(service=callservice)

calldriver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Selecing textbox name and adding some text 
calldriver.find_element(by=By.ID,value="name").send_keys("mynewpractice")
time.sleep(2)

# Clicking on the button
calldriver.find_element(by=By.XPATH,value="//input[@class='btn-style']").click()
time.sleep(2)

# swithcing to alerts
popuphandle = calldriver.switch_to.alert
time.sleep(2)
print(popuphandle.text)
time.sleep(2)

validatetext = popuphandle.text
assert "mynewpractice" in validatetext

popuphandle.accept()

# Selecing textbox name and adding some text 
calldriver.find_element(by=By.ID,value="name").send_keys("mynewpractice")
time.sleep(2)

# Clicking on the button
calldriver.find_element(by=By.XPATH,value="//input[@id='confirmbtn']").click()
time.sleep(2)

popuphandle.dismiss()

calldriver.close()