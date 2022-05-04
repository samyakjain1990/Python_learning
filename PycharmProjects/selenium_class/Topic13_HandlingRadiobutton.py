from subprocess import call
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

callservice = ChromeService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")
calldriver = webdriver.Chrome(service=callservice)

calldriver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Click on radio button using xpath
calldriver.find_element(by=By.XPATH,value="//input[@value='radio2']").click()

time.sleep(2)

#clicking on the radio button using css selector
calldriver.find_element(by=By.CSS_SELECTOR,value="input[value='radio1']").click()

time.sleep(2)

# we can even store all the radio button in one list and select the one with radio3

radiobuttonlist= calldriver.find_elements(by=By.XPATH,value="//input[@type='radio']")

print(len(radiobuttonlist))

for radiobutton in radiobuttonlist:
    if radiobutton.get_attribute("value") == "radio3":
        radiobutton.click()

calldriver.close()