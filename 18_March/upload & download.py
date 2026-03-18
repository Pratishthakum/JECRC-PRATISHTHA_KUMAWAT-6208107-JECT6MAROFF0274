from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
sleep(2)

upload_file = driver.find_element(By.XPATH,'//a[text()="File Upload"]')
upload_file.click()

choose_file_button = driver.find_element(By.ID,'file-upload')
choose_file_button.send_keys(r'C:\Users\neera\Downloads\file1.txt')
sleep(4)
driver.find_element(By.ID,'file-submit').click()
driver.back()
driver.back()
download_file = driver.find_element(By.XPATH,'//a[text()="File Download"]')
download_file.click()
driver.find_element(By.XPATH,'//a[text()="file1.txt"]').click()
sleep(5)
driver.quit()