#Task 1

#https://codepen.io/gdw96/pen/jOypoYL

'''

1. navigate to the above url
2. enter username and password
3. click on hold on the eye to view password
4. click on register
5. Use sleep for 5sec then refresh the page
6. Validate the word `Registration` using assert

'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()


driver.get("https://codepen.io/gdw96/pen/jOypoYL")

# driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@id="result"]'))

username=driver.find_element(By.ID,'username')
username.send_keys("Pratishtha")
sleep(2)

email=driver.find_element(By.XPATH,'//input[@id="email"]')
email.send_keys("prati123@gmail.com")
sleep(2)

password=driver.find_element(By.ID,'password')
password.send_keys("12345")
sleep(2)

eye_icon=driver.find_element(By.XPATH,'//button[@id="showPsswd"]')

actions=ActionChains(driver)
actions.click_and_hold(eye_icon).perform()

sleep(2)
actions.release().perform()


Register=driver.find_element(By.XPATH,'//input[@type="submit"]')
Register.click()



sleep(5)

driver.refresh()
driver.back()


iframe=driver.find_element(By.ID,'result')
driver.switch_to.frame(iframe)
ele01=driver.find_element(By.TAG_NAME,"h1")
assert 'Registration' in ele01.text, "Couldn't find registration page"
print("Registration successfully")









