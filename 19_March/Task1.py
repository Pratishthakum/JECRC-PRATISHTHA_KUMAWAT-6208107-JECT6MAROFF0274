'''
Task 1

### abc.com To fetch banner images

1. Go to abc.com
2. Find the banners
3. Print the image links

'''


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://abc.com/')
driver.maximize_window()
wait01=WebDriverWait(driver,10)
Banners_visible= wait01.until(EC.presence_of_all_elements_located((By.XPATH ,'//div[@id="hero-items"]/descendant::img[@data-mptype="image"]')))
for b in Banners_visible:
    print(b.get_attribute('src'))
