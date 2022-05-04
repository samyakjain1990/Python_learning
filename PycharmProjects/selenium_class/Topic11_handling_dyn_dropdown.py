from subprocess import call
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

callservice = ChromeService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")
calldriver = webdriver.Chrome(service=callservice)

calldriver.get("https://rahulshettyacademy.com/dropdownsPractise/")

calldriver.find_element(by=By.ID,value="autosuggest").send_keys("Ind")
time.sleep(2)

# taking control over dynamic dropdown
dydropdown = calldriver.find_elements(by=By.XPATH,value="//li[@class='ui-menu-item']/a")
print(len(dydropdown))

for itemdropdown in dydropdown:
    if itemdropdown.text == "India":
        itemdropdown.click()
        break
    else:
        print("Item not found")

# This print of the text will not work in this case becuase selenium DOM takes input of all the elements when pages gets loaded
# and this text is not known
print(calldriver.find_element(by=By.ID,value='autosuggest').text)

assert calldriver.find_element(by=By.ID,value='autosuggest').get_attribute('value') == "India"