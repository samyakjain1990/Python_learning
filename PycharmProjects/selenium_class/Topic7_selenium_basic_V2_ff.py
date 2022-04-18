"""
In this version of basic selenium we are using "Driver Management Software" + service
With this new way we need not download the webdriver manually it is automaticaly downloaded according to the browser
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time  

Service1 = FirefoxService(executable_path=GeckoDriverManager().install())
Driver1 = webdriver.Firefox(service = Service1)

Driver1.get("https://www.instagram.com")
print(Driver1.current_url)
print(Driver1.current_window_handle)


time.sleep(2)

Driver1.close()