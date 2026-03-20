
"""
* conditional waits - implicit and explicit
1. explicit - we can give multiple conditions

2. implicit (waits for a certain period of time to find that element,if element is not found at the nth second then it returns element not found exception ,works only for driver.find_element method, wont work for any other method)
implicit wait is only used for find element
implicit wait still works if element is hidden on the screen , can find all elements present in DOM structure
implicit waits are global

* unconditional waits
"""
#waits are used to handle synchronization issues, situations where your DOM structure has already loaded but the UI hasn't
#basically there is a time gap between the loading of both the components

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://abc.com/')
driver.maximize_window()
driver.implicitly_wait(5)

element1=driver.find_element(By.XPATH,'//span[text()="American Idol"]')
print("Found the American Idol")