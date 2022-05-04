"""
Handling frames
# in case if you are not able to use some locator so do check if that contains any of the below tags
frameset, iframe or frame
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

callservice = ChromeService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")
Calldriver = webdriver.Chrome(service=callservice)

Calldriver.get("https://rahulshettyacademy.com/AutomationPractice/")

# switch to frames
Calldriver.switch_to.frame("courses-iframe")
# clicking on button
Calldriver.find_element(By.XPATH,value="//a[text()='Courses']").click()