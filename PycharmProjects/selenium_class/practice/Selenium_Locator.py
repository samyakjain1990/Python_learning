"""
There are 3 different ways to use browser driver in selenium
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
"""

# This can be used where system has complete internet connection and python can download the driver compatibile with your browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import time

'''
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
'''


service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# open an URL
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)

driver.find_element(By.NAME,value= "name").send_keys("Rahul Shetty")
time.sleep(2)

#driver.find_element(By.NAME,value= "email").send_keys("rahul123@gmail.com")
driver.find_element(By.CSS_SELECTOR,value="input[name='email']").send_keys("abcd@gmail.com")
time.sleep(2)

#driver.find_element(By.ID,value="exampleInputPassword1").send_keys("mynameisrahul")
driver.find_element(By.CSS_SELECTOR,value="input[class='form-control']").send_keys("mynameissamyakjain")
time.sleep(2)

driver.find_element(By.ID,value="exampleCheck1").click()
time.sleep(2)

driver.close()