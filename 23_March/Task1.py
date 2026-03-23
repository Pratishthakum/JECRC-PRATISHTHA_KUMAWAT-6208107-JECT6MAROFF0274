#Task1: open fav website then scroll down to fav picture then scroll uo 5 times back and forth comes to image and then go up then come to image

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome()
driver.get("https://www.chennaisuperkings.com/")
driver.maximize_window()
action=ActionChains(driver)
img=driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[4]/div/app-homepage-gallery-card/div/div/div[1]/img[2]')
action.scroll_to_element(img).perform()
sleep(5)
for i in range(5):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(3)






