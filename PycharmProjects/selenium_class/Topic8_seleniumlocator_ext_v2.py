from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

callservice = ChromeService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")
calldriver = webdriver.Chrome(service=callservice)

calldriver.get("https://login.salesforce.com")


# smart CSS only for ID attribute 
# tagname#ID (tagname is optional and can we skipped also)
calldriver.find_element(by=By.CSS_SELECTOR,value="input#username").send_keys("test@cisco.com")
time.sleep(2)

# tagname.classname (there should not be any spaces in className.Replace with .)
calldriver.find_element(by=By.CSS_SELECTOR,value="input.password").send_keys("justpassword")
time.sleep(2)

# clearing any textbox
calldriver.find_element(by=By.CSS_SELECTOR,value="input#username").clear()
time.sleep(2)

# clicking link text
# Enter the text which you want to clicked
# Remember both LINK_TEXT and PARTIAL LINK TEXT only work if tag is "a" which refers to link
calldriver.find_element(by=By.LINK_TEXT,value="Forgot Your Password?").click()
time.sleep(2)

calldriver.back()
time.sleep(2)

# clicking partial text link
calldriver.find_element(by=By.PARTIAL_LINK_TEXT,value="Use Custom").click()
time.sleep(2)

calldriver.close()