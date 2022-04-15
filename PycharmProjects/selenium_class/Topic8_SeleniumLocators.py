"""
There are 3 different ways to use browser driver in selenium
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
"""

from itertools import dropwhile
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice") 

# maximize thr window
driver.maximize_window()

# Enter the value after finding the name attribute
driver.find_element_by_name("name").send_keys("dabba")

# Enter the value after finding by emailid
driver.find_element_by_name("email").send_keys("abcd.gmai.com")

# Enter the value using the ID
driver.find_element_by_id("exampleInputPassword1").send_keys("qwerty@123")

# Checking the checkbox 
driver.find_element_by_id("exampleCheck1").click()

# finding the element by css element 
# tagname[attribute='value']
# ex - [attribute*='value']
driver.find_element_by_css_selector("input[name='name']").send_keys("ABCD")

# finding the element by css element [regular expression]
#driver.find_element_by_css_selector("div[class*='alert-success']").text
# finding the element by css element [regular expression but without tag name]
#driver.find_element_by_css_selector("[class*='alert-success']").text

Dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
Dropdown.select_by_index(1)
Dropdown.select_by_visible_text("Male")

# finding the element using the xpath
# //tagname[@attribute='value']
# //*[contains(properties,'')] 
driver.find_element_by_xpath("//input[@type='submit']").click()
# checking the xpath using the regular expression
#driver.find_element_by_xpath("[//*(contains,'alert-success')]").text

#value = driver.find_element_by_class_name("alert-success").text

#time.sleep(10)

#driver.close()

# find the CSS path for the element to be selected

