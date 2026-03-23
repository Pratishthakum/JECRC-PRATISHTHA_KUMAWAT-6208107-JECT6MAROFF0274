#handling actions of mouse and keyboard

from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

opts=ChromiumOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/drag_and_drop')
driver.maximize_window()
sleep(3)

action=ActionChains(driver)

orignal_element=driver.find_element(By.ID,'column-a')
target_element=driver.find_element(By.ID,'column-b')

action.drag_and_drop(orignal_element,target_element).perform()
sleep(5)

#mouse mover
driver.get('https://supertails.com/')
action=ActionChains(driver)
doggo=driver.find_element(By.XPATH,'(//span[contains(text(),"Dogs")])[1]')
action.move_to_element(doggo).perform()
sleep(3)

driver.quit()