from selenium import webdriver 

driver = webdriver.Chrome("/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")

driver.get("https://rahulshettyacademy.com/")

print(driver.current_url)
print(driver.title)