


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
animals=driver.find_element(By.CSS_SELECTOR,'select[id="animals"]')
animals2=driver.find_element(By.CSS_SELECTOR,'#animals')
form_control=driver.find_element(By.CSS_SELECTOR,'.form-control')
print('id animals found')
print(animals,animals2,form_control)

home=driver.find_element(By.CSS_SELECTOR,'a[href*="testautomationpractice"]')
print("finished running the script")

links=driver.find_elements(By.CSS_SELECTOR,'a[href^="http://"]')
print(links)
print(len(links))

links2=driver.find_elements(By.CSS_SELECTOR,'a[href$=".com"]')
print(links2)
print(len(links2))

links3=driver.find_elements(By.CSS_SELECTOR,'div[class="widget-content"] a[href$=".com"]')
print(links3)
print(len(links3))

result=driver.find_elements(By.CSS_SELECTOR,'input[class="form-control"][id="email"]')
print(result)
print(len(result))