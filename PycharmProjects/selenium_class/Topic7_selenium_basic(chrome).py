"""
There are 3 different ways to use browser driver in selenium
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
"""

# The below way of using executable path is deprecated


from selenium import webdriver 
import time

driver = webdriver.Chrome(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")

driver.get("https://rahulshettyacademy.com/")                                           # URL to open
print(driver.current_url)                                                               # print the current URL
print(driver.title)                                                                     # print the current title

# Sleeing for 10 seconds
time.sleep(10)

driver.get("https://rahulshettyacademy.com/AutomationPractice")                         # URL to open
print(driver.current_url)                                                               # print the current URL
print(driver.title)                                                                     # print the current title

driver.back()                                                                           # going back to the HOME page 

# sometimes with refresh close does not work 
driver.refresh()                                                                        # refreshing the page
driver.close()