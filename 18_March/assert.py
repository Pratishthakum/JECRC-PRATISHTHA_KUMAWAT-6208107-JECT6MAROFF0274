
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(5)
eyeglass = driver.find_element(By.ID,'lrd1')
# print(eyeglass.text)
assert 'EYE' in eyeglass.text, 'could not find the element'
print('successful assert 1')
brand_name = driver.find_element(By.XPATH,'//h3[@class="sc-5c474d1e-0 gcOylD"]')
assert 'Top' in brand_name.text, 'could not find the element'
print('successful assert 2')
driver.get('https://www.lenskart.com/lenskart-studio-lk-s18862-c1-sunglasses.html')
sleep(3)
driver.find_element(By.XPATH,'//p[@title="Enter pincode"]').click()

sleep(5)
driver.quit()
