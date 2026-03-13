from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
# opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(5)
element1=driver.find_element(By.XPATH,'//input[@maxlength="15"]')
element2=driver.find_element(By.XPATH,'//label[@for="gender"]')
element3=driver.find_element(By.XPATH,'//button[@type="submit"]')
element4=driver.find_element(By.XPATH,'//input[@placeholder="End Date"]')
element5=driver.find_element(By.XPATH,'//style[@type="text/css"]')
print(element1)
print(element2)
print(element3)
print(element4)
print(element5)
print("Script  terminated")

#inner text in xpath
element6=driver.find_element(By.XPATH,'//a[text()="Home"]')
element7=driver.find_element(By.XPATH,'(//a[text()="Home"])[1]')
element8=driver.find_element(By.XPATH,'//a[text()="GUI Elements"]')
element9=driver.find_element(By.XPATH,'//label[text()="Email:"]')

#using contains
element10=driver.find_element(By.XPATH,'//label[contains(text(),"Male")]')
element11=driver.find_element(By.XPATH,'//option[contains(text(),"Blue")]')