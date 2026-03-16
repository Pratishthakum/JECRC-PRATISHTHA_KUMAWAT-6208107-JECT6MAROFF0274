from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
name=driver.find_element(By.ID ,'name')
name.clear()
name.send_keys('Pratishtha')
sleep(1)
Email=driver.find_element(By.XPATH ,'//input[@placeholder="Enter EMail"]')
Email.send_keys('pratishthakumawat23@gmail.com')
click1=driver.find_element(By.ID ,'male').click()
ele1=driver.find_element(By.XPATH , '//label[text()="Monday"]/preceding-sibling::input').click()
monday_checkbox=driver.find_element(By.XPATH , '//input[@id="monday"]/following-sibling::label')
print(monday_checkbox.text)#returns inner text

sleep(6)
print(name.get_attribute('placeholder'))
print(name.get_attribute('value'))
print(Email.get_attribute('placeholder'))
driver.quit()





