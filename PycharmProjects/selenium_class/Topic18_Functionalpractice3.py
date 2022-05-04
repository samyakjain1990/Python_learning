"""
Verify if sum of products in checkout page matches with total amount 

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

# navigating to new page
# valiudating if the items are correctly added or not
assert itemcountinitial == itemcountlater

# storing the initial amount  
beforedisAmt = Calldriver.find_element(by=By.XPATH,value="//span[@class='totAmt']").text

#Applying discount
Calldriver.find_element(by=By.CSS_SELECTOR,value="input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")
Calldriver.find_element(by=By.CSS_SELECTOR,value="button[class='promoBtn']").click()

wait = WebDriverWait(Calldriver,7)
wait.until(EC.presence_of_element_located((By.CLASS_NAME,"promoInfo")))

afterdisAmt = Calldriver.find_element(by=By.CSS_SELECTOR,value="span[class='discountAmt']").text

assert float(afterdisAmt) < float(beforedisAmt)

# Validating if the product price amount total is similar to the "Total Amount"

eachcommditytotal = Calldriver.find_elements(by=By.XPATH,value="//tr/td[5]/p")

sum = 0

for eachcommdity in eachcommditytotal:
    sum = sum + int(eachcommdity.text)

print(sum)

assert sum == int(beforedisAmt)

Calldriver.close()
