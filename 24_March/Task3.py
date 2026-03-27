# Task 3
# ### Windows
# 1. navigate to the url: `https://demoqa.com/browser-windows`
# 2. work on all the 3 windows one after the other
# 3. validate the text result appearing, you should use assert with it the result shown


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/browser-windows')
driver.maximize_window()

parent_window=driver.current_window_handle

#new tab
driver.find_element(By.ID,'tabButton').click()
sleep(2)
all_windows=driver.window_handles
driver.switch_to.window(all_windows[1])

assert 'This is a sample page' in driver.find_element(By.ID,'sampleHeading').text, 'Page not found'

#new window
driver.switch_to.window(parent_window)
driver.find_element(By.ID,'windowButton').click()
all_windows=driver.window_handles
driver.switch_to.window(all_windows[2])
assert 'This is a sample page' in driver.find_element(By.ID,'sampleHeading').text, 'Page not found'

#new window message
driver.switch_to.window(parent_window)
driver.find_element(By.ID,'messageWindowButton').click()
all_windows=driver.window_handles
driver.switch_to.window(all_windows[3])
assert 'Knowledge' in driver.find_element(By.TAG_NAME,'body').text, 'Error'
driver.quit()


