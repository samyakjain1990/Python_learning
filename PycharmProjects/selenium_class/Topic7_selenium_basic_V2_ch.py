"""
In this version of basic selenium we are using "Driver Management Software" + service
With this new way we need not download the webdriver manually it is automaticaly downloaded according to the browser
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

service1 = ChromeService(executable_path=ChromeDriverManager().install())
driver1 = webdriver.Chrome(service=service1)

driver1.get("https://www.facebook.com")
print(driver1.current_url)
print(driver1.current_window_handle)


driver1.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
print(driver1.current_url)
print(driver1.title)
driver1.back()

time.sleep(2)

driver1.close()