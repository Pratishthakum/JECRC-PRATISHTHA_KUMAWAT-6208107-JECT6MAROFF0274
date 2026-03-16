# 1.navigate to flipkart
# 2.find search field and search for a product
# 3.get attribute of product search
# 4.click on search button
# 5.click on a check  box or boxes in filter
# 6.get the text of that filter

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://www.flipkart.com')
driver.maximize_window()
sleep(1)

#clicking on cross
driver.find_element(By.XPATH,'//span[@role="button"]').click()

#searching a product and getting attributes
search_field=driver.find_element(By.XPATH,"//input[@name='q']")
search_field.send_keys('Laptop')
print(search_field.get_attribute('value'))
print(search_field.get_attribute('type'))
print(search_field.get_attribute('title'))
driver.find_element(By.XPATH,'//button[@type="submit"]').click()

#click on a checkbox
driver.find_element(By.XPATH,'//div[@class="ybaCDx"]').click()

#print src of the first image that comes when u search
image1=driver.find_element(By.XPATH,'//div[@class="lWX0_T"]/descendant::img')
print(image1.get_attribute('src'))





