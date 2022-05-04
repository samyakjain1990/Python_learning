from tabnanny import check
from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By


callservice = FirefoxService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/geckodriver")
calldriver = webdriver.Firefox(service=callservice)

calldriver.get("https://rahulshettyacademy.com/AutomationPractice/")

findcheckbox = calldriver.find_elements(by=By.XPATH,value="//input[@type='checkbox']")
# finding the lenth of the checkbox
print(len(findcheckbox))

# looping through all the checkbox in the page and clicking them
for checkbox in findcheckbox:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

calldriver.close()