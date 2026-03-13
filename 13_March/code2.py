from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

sleep(5)

# ID
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
submit = driver.find_element(By.ID, "submit")

print("ID elements found")

# CLASS
title = driver.find_element(By.CLASS_NAME, "post-title")
print(title.text)

print("Class element found")

# TAG
heading = driver.find_element(By.TAG_NAME, "h1")
print("Tag element:", heading.text)



driver.quit()


