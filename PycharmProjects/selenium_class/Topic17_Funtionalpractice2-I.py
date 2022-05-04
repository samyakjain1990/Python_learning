"""
Verify after applying discount the price decrease

a) the way to solve this problem is to take the price from each product tag and sum it up
b) verify the price on the second page if that is less then current sum
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
    itemsum = button.find_element(by=By.XPATH,value="//p[@class='product-price']").text
    print(itemsum)
    #MRPsum = MRPsum + itemsum

#print(MRPsum)