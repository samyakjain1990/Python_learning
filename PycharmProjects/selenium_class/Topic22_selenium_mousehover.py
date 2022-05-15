"""
As a part of the we are going to use actions class for handling mouse hover and clicking on any button or getting any text

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

callservice = ChromeService(executable_path="/Users/samyjain/Python_learning/PycharmProjects/selenium_class/chromedriver")
driver = webdriver.Chrome(service=callservice)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# here we are going to use action class

hoverclass = ActionChains(driver)
menu = driver.find_element(by=By.ID,value='mousehover')
hoverclass.move_to_element(menu).perform()

# now hover and click another child item
childhover = driver.find_element(by=By.LINK_TEXT,value="Top")
hoverclass.move_to_element(childhover).click().perform()

# now again going and hovering over mouse hover
hoverclass.move_to_element(menu).perform()

# now hover and click another child item
childhover1 = driver.find_element(by=By.LINK_TEXT,value="Reload")
hoverclass.move_to_element(childhover1).click().perform()

driver.close()