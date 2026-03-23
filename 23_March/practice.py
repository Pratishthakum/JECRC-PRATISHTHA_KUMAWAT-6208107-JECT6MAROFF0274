from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

opts=ChromiumOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome()
driver.get('https://demoqa.com/droppable')
driver.maximize_window()
sleep(3)

wait=WebDriverWait(driver,5)
draggable_element=wait.until(ec.visibility_of_element_located((By.ID,'draggable')))
droppable_element=wait.until(ec.visibility_of_element_located((By.ID,'droppable')))

action=ActionChains(driver)
action.drag_and_drop(draggable_element,droppable_element).perform()
sleep(3)

validation=wait.until(ec.visibility_of_element_located((By.XPATH,'//div[@id="droppable"]/p')))
assert validation.text=='Dropped!', 'Error'




