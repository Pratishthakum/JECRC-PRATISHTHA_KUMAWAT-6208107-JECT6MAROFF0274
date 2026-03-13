from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
# opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(3)
name=driver.find_element(By.ID,'name')
print(name)
print('name textfield found')

phone_number=driver.find_element(By.ID,'phone')
print('phone number textfield found')
navbar=driver.find_element(By.NAME,'Navbar')
print('Navigation bar  found')
radio_button=driver.find_element(By.CLASS_NAME,'form-check-input')
print('radio button found')
radio_buttons=driver.find_elements(By.CLASS_NAME,'form-check-input')
print(radio_buttons)
print(len(radio_buttons))
print('radio buttons found')
input_elements=driver.find_elements(By.TAG_NAME,'input')
print(input_elements)
print(len(input_elements))
driver.quit()

