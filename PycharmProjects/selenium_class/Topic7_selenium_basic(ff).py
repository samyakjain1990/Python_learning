"""
There are 3 different ways to use browser driver in selenium
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
"""

from selenium import webdriver

newdriver= webdriver.Firefox(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/geckodriver")

newdriver.get("https://rahulshettyacademy.com/")
print(newdriver.current_url)
print(newdriver.title)

newdriver.close()