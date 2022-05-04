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

# Open the URL
Calldriver.get("https://the-internet.herokuapp.com/iframe")

# switch to frame with passing the frameid or any locator
Calldriver.switch_to.frame("mce_0_ifr")

# clearing up the whole frame
Calldriver.find_element(By.XPATH,value="//body[@id='tinymce']").clear()
# adding data to the frame
Calldriver.find_element(By.XPATH,value="//body[@id='tinymce']").send_keys("my name is anthony")

# now to switch back to the old html code you need to switch back
Calldriver.switch_to.default_content()

print(Calldriver.find_element(By.TAG_NAME,value="h3").text)


Calldriver.close()