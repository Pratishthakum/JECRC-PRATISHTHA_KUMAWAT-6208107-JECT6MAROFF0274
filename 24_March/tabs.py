from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
sleep(2)
parent_window=driver.current_window_handle
print(parent_window)
driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
sleep(2)

all_windows=driver.window_handles
print(len(all_windows))

driver.switch_to.window(all_windows[-1])

assert 'New' in driver.find_element(By.CLASS_NAME,'example').text
# print("done")
driver.close()

driver.switch_to.window(parent_window)



#opening a website in new window
driver.switch_to.new_window('window')
sleep(3)
driver.get("https://www.cricbuzz.com/")

# driver.switch_to.new_window('tab')
# sleep(2)
# driver.get("https://www.cricbuzz.com/")

