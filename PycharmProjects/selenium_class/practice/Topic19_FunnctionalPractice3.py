"""
Verify if the search funtionality in home page 
is working or not

Ber = 3 products
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


products = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']

callservice = ChromeService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")
Calldriver = webdriver.Chrome(service=callservice)

Calldriver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

Calldriver.find_element(by=By.XPATH,value="//input[@type='search']").send_keys("ber")
Calldriver.implicitly_wait(10)

