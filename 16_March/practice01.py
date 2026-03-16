
#Task: toggle between male and female using loops


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
genders = driver.find_elements(By.NAME,"gender")

for gender in genders:
    gender.click()
    sleep(2)