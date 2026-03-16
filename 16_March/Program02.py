from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in/')
sleep(2)

driver.maximize_window()

search=driver.find_element(By.ID,'twotabsearchtextbox')
search.clear()
search.send_keys('accessories')
sleep(2)
search.clear()
search.send_keys('samsung s25')
search_button=driver.find_element(By.ID,'nav-search-submit-button')
search_button.click()
sleep(2)
search01=driver.find_element(By.ID,'twotabsearchtextbox')
search01.clear()

print(search01.get_attribute('id'))

search01.send_keys('mobiles')
print(search01.get_attribute('value'))
driver.find_element(By.ID,'nav-search-submit-button').click()

sleep(1)
driver.quit()



print(search.get_attribute('placeholder'))
print(search.get_attribute('value'))

driver.quit()