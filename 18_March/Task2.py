## Task 2
### Registration Form
# 1. Go to: https://demoqa.com/automation-practice-form
# 2. Handle every element in that form except the calendar
# `Note: Give fake names and emails`
# 3. Click on submit button

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()
sleep(2)
first_name = driver.find_element(By.ID,'firstName')
first_name.send_keys('abc')
sleep(2)
last_name = driver.find_element(By.ID,'lastName')
last_name.send_keys('def')
sleep(2)
email_ID = driver.find_element(By.ID,'userEmail')
email_ID.send_keys('abcdefd@gmail.com')
sleep(2)
gender=driver.find_element(By.ID,'gender-radio-2')
gender.click()
sleep(2)
phone_no = driver.find_element(By.ID,'userNumber')
phone_no.send_keys('0123456789')
sleep(2)
checkboxes = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
sleep(1)
for i in range(0,len(checkboxes)):
    if i==0:
        continue
    checkboxes[i].click()
    sleep(1)
upload = driver.find_element(By.ID,'uploadPicture')
upload.send_keys(r'C:\Users\Dell\Downloads\photo01.jpg')
sleep(2)
address_filed = driver.find_element(By.ID,'currentAddress')
address_filed.send_keys('226 asdf, sdfghjkl, hjklihgfx')
state = driver.find_element(By.ID,'react-select-3-input')
state.send_keys('Rajasthan',Keys.ENTER)
city = driver.find_element(By.ID,'react-select-4-input')
city.send_keys('Jaipur',Keys.ENTER)
submit_button = driver.find_element(By.ID,'submit')
submit_button.click()
sleep(5)
driver.quit()


