from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")

driver.get("https://login.salesforce.com/")

driver.find_element_by_name("username").send_keys("abcd")

# find the element using the <tagname#id> 
# this is only valid in case of id
# smartcss is the good way to find it and it is faster
driver.find_element_by_css_selector("input#username").send_keys("asdsadas")
driver.find_element_by_css_selector("#username").send_keys("sad")

# using 2 attributes in xpath
driver.find_element_by_xpath("//*[@type='email'][@name='username']").send_keys("asdasdsadsad")
driver.find_element_by_xpath("//*[@type='email']").clear()

# clicking on the link text
#driver.find_element_by_link_text("Forgot Your Password?").click()
#driver.find_element_by_xpath("//*[@value='Cancel']").click()

time.sleep(5)

findele = driver.find_element_by_id("signup_link")

print(findele)

if findele:
   driver.find_element_by_id("signup_link")

#if 