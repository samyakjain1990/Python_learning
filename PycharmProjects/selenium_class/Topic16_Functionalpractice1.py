"""
Validate whether products selected in Page1 
are showing up in Page2 Check page

there 2 ways of doing this 
a) run for loop
    1) loop for clicking on the "add to cart button"
    2) loop to find the name using the text property

b) run for loop once and do both of things together

New thing to learn in this topic is traversing back from an element which is only possible with xpath 
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

itemcountinitial = []

callservice = ChromeService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")
Calldriver = webdriver.Chrome(service=callservice)

Calldriver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

Calldriver.find_element(by=By.XPATH,value="//input[@type='search']").send_keys("ber")
Calldriver.implicitly_wait(10)

buttons = Calldriver.find_elements(by=By.XPATH,value="//div[@class='product']/div/button")

for button in buttons:
    button.click()
    # append is used here to push the values in list
    # //div[@class='product']/div/button/parent::div/parent::div/h4
    itemcountinitial.append(button.find_element(by=By.XPATH,value="parent::div/parent::div/h4").text)

print(itemcountinitial)

Calldriver.find_element(by=By.XPATH,value="//img[@alt='Cart']").click()

Calldriver.find_element(by=By.XPATH,value="//button[text()='PROCEED TO CHECKOUT']").click()

# waiting for the page to be displayed
wait= WebDriverWait(Calldriver,5)
wait.until(EC.presence_of_element_located((By.CLASS_NAME,"promoCode")))

itemcountlater = []

finditemname = Calldriver.find_elements(by=By.XPATH,value="//p[@class='product-name']")

for finditem in finditemname:
    itemcountlater.append(finditem.text)

print(itemcountlater)

assert itemcountinitial == itemcountlater
# navigating to new page
# valiudating if the items are correctly added or not



