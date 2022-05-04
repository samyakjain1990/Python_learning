"""
Implicit Sleep

<driver>.implicitly_wait(5)

Explicit Sleep

#explicit waitking for a element to show up
wait = WebDriverWait(<driver>,5)
wait.until(EC.presence_of_all_elements_located(By.CLASS_NAME,Value= "promoCode"))

we need to import a package for explicit wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""

from http.server import executable
from multiprocessing.sharedctypes import Value
from subprocess import call
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

callservice = FirefoxService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/geckodriver")
calldriver = webdriver.Firefox(service=callservice)
# implicit wait and this is a global wait
calldriver.implicitly_wait(15)

calldriver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

calldriver.find_element(by=By.XPATH,value="//input[@type='search']").send_keys("ber")
time.sleep(5)

numberofbuttonform = len(calldriver.find_elements(by=By.XPATH,value="//div[@class='products']/div"))

print(numberofbuttonform)
assert numberofbuttonform == 3

clickonbuttons = calldriver.find_elements(by=By.XPATH,value="//div[@class='product-action']/button")
print(len(clickonbuttons))

for clickbutton in clickonbuttons:
    clickbutton.click()

time.sleep(2)

calldriver.find_element(by=By.XPATH,value="//img[@alt='Cart']").click()

calldriver.find_element(by=By.XPATH,value="//button[text()='PROCEED TO CHECKOUT']").click()

#explicit waitking for a element to show up
wait = WebDriverWait(calldriver,5)
wait.until(EC.presence_of_element_located(By.CLASS_NAME,"promoCode"))


calldriver.find_element(by=By.CSS_SELECTOR,value="input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")
calldriver.find_element(by=By.CSS_SELECTOR,value="button.promoBtn").click()

print(calldriver.find_element(by=By.CSS_SELECTOR,value="span.promoInfo").text)





    