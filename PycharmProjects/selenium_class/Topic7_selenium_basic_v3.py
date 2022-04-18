"""
There are 3 different ways to use browser driver in selenium
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

In this version of basic selenium we are using hardcoded chromedriver location + service
"""

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")
driver = webdriver.Chrome(service=service)


driver.get("https://www.facebook.com")
time.sleep(10)


driver.close()