from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
driver.get(" https://the-internet.herokuapp.com/login")
driver.maximize_window()
element1=driver.find_element(By.XPATH, '//input[@name="username"]')
print(element1)
element2=driver.find_element(By.XPATH,'//input[@id="password"]')
print(element2)
element3=driver.find_element(By.XPATH, '//button[@type="submit"]')
print(element3)
element4=driver.find_element(By.XPATH , '//a[text()="Elemental Selenium"]')
print(element4)
element5 = driver.find_element(By.XPATH,'//h2[contains(text(),"Login Page")]')
print(element5)

sleep(5)
driver.quit()








