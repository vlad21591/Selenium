from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Accessing the web-page
driver = webdriver.Chrome()
driver.get('http://www.google.com')
# Finding the relevant element
element = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
time.sleep(3)
element.clear()
# Required input
element.send_keys('Naudaq')
element.send_keys(Keys.RETURN)
time.sleep(3)
# Using the return button
driver.back()
time.sleep(3)
element = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
time.sleep(3)
element.clear()
element.send_keys('Nasdaq Stocks')
element.send_keys(Keys.RETURN)
print(driver.current_url)