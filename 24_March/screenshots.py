import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

folder=os.path.join(os.getcwd(),'screenshots')
os.makedirs(folder,exist_ok=True)


driver=webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()

sleep(2)

driver.save_screenshot(f'{folder}/full_page.png')
sleep(3)
action=ActionChains(driver)
ele=driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"]/descendant::img)[3]')
#//img[contains(@alt,"Photo of a woman in cherry-patterned")]

action.scroll_to_element(ele).perform()
sleep(1)

ele.screenshot(f'{folder}/cherry_red.png')
sleep(7)


