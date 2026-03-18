from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(3)

male_button = driver.find_element(By.ID,'male')
male_button.click()
check_box = driver.find_element(By.XPATH,'//label[text()="Days:"]/following-sibling::div/input')
check_box.click()
print(male_button.is_enabled()) ## used for button to check enabled or not
print(male_button.is_displayed()) ## check if it is visible on UI
print(check_box.is_selected())
driver.quit()