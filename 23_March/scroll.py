from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



driver=webdriver.Chrome()
driver.get("https://supertails.com/")
driver.maximize_window()
action=ActionChains(driver)

catto=driver.find_element(By.XPATH,'//div[@data-ganame="Breed 5"]')
action.scroll_to_element(catto).perform()
sleep(5)



action.scroll_by_amount(0,-500).perform()

sleep(5)

action.scroll_by_amount(0,500).perform()
sleep(3)


action.context_click(catto).perform()
sleep(3)

action.double_click(catto).perform()
sleep(2)


action.send_keys(Keys.PAGE_UP).perform()
sleep(5)
action.key_down(Keys.CONTROL).send_keys('a').perform()
sleep(2)
action.key_up(Keys.CONTROL).perform()
sleep(2)
action.key_down(Keys.CONTROL).send_keys('c').perform()
sleep(2)





#copy and paste
driver=webdriver.Chrome()
driver.get(r'C:\Python\Testing\selenium\23_March\Project.html')
driver.maximize_window()
action=ActionChains(driver)

present=driver.find_element(By.ID,'presentAddress')
permanent=driver.find_element(By.ID,'permanentAddress')
present.send_keys('JECRC, JAIPUR, RJ')
sleep(2)
present.click()
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
permanent.click()
sleep(2)
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
sleep(5)






driver.quit()


# action.scroll_from_origin(0,0,1000).perform()
# sleep(5)