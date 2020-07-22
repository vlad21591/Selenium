from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.facebook.com')
# Entering personal data
email_or_phone = driver.find_element_by_xpath('//*[@id="email"]')
email_or_phone.send_keys('1234@gmail.com')
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('demo12345')
login_Key = driver.find_element_by_xpath('//*[@id="u_0_b"]')
login_Key.click()
# Finding the message bar
post_element = driver.find_element_by_xpath("//*[@name='xhpc_message']")
time.sleep(3)
# Required message
post_element.send_keys('Hello Facebook')
time.sleep(3)
buttons = driver.find_element_by_tag_name('button')
time.sleep(3)
# Finding the Post button from all the buttons
for button in buttons:
    if button.text == ' Post':
        button.click()
