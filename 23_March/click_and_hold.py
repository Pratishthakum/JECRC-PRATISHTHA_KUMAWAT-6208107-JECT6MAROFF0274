from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver=webdriver.Chrome()
driver.get(r'file:///C:/Users/Dell/Downloads/index1.html')
driver.maximize_window()
action=ActionChains(driver)


driver.find_element(By.ID,'password').send_keys('pratishtha')
sleep(3)
show_pad=driver.find_element(By.ID,'eyeBtn')
action.click_and_hold(show_pad).perform()
sleep(3)
action.release()

driver.quit()


