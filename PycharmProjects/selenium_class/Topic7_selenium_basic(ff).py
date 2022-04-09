from selenium import webdriver


newdriver= webdriver.Firefox(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/geckodriver")

newdriver.get("https://rahulshettyacademy.com/")
print(newdriver.current_url)
print(newdriver.title)

newdriver.close()