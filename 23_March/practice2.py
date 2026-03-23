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

Prevent_propagation=driver.find_element(By.ID,'droppableExample-tab-preventPropogation')
Prevent_propagation.click()
wait=WebDriverWait(driver,5)
dragbox=wait.until(ec.presence_of_element_located((By.ID,'dragBox')))
outer_box=wait.until(ec.presence_of_element_located((By.ID,'notGreedyDropBox')))
inner_box=wait.until(ec.presence_of_element_located((By.ID,'notGreedyInnerDropBox')))

action=ActionChains(driver)
action.drag_and_drop(dragbox,outer_box).perform()
action.drag_and_drop(dragbox,inner_box).perform()
sleep(4)
