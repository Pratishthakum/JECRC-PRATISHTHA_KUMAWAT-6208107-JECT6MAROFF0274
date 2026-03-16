from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.get("https://opensource-demo.orangehrmlive.com/")
sleep(3)
print("The title of the web page is", driver.title)
username=driver.find_element(By.XPATH , '//input[@placeholder="Username"]')
username.clear()
username.send_keys("Admin")
username.send_keys(Keys.ENTER)
Password=driver.find_element(By.XPATH , '//input[@placeholder="Password"]')
Password.send_keys("admin123")
Password.send_keys(Keys.ENTER)
sleep(3)
current_url=driver.current_url
print("current url: ",current_url)
if "dashboard" in current_url:
    print("successful login")
sleep(3)
driver.quit()





