'''
Task2: !.go to myntra
2.hover over men or women
3.choose a category then click on it
4.scroll through the 4th or 5th row product
5.(use proper waits)
'''




from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


opts=ChromiumOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.myntra.com/')
driver.maximize_window()
sleep(2)

wait=WebDriverWait(driver,5)
action=ActionChains(driver)
women=wait.until(ec.visibility_of_element_located((By.XPATH,'(//div[@class="desktop-navLink"])[2]/a')))
action.move_to_element(women).perform()

category=wait.until(ec.visibility_of_element_located((By.XPATH,'//li[@data-reactid="218"]')))
category.click()

fourth=wait.until(ec.presence_of_element_located((By.XPATH,'(//ul[@class="results-base"]/li)[16]')))
action.scroll_to_element(fourth).perform()

sleep(10)
driver.quit()


