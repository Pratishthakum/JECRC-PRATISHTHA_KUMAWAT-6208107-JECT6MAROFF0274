from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://qavbox.github.io/demo/signup/')
driver.maximize_window()
wait = WebDriverWait(driver, 5, poll_frequency=0.5)

Fullname = wait.until(EC.visibility_of_element_located((By.ID, 'username')))
Fullname.send_keys('abc')

email = wait.until(EC.visibility_of_element_located((By.ID, 'email')))
email.send_keys('abc@gmail.com')

number=wait.until(EC.visibility_of_element_located((By.ID,'tel')))
number.send_keys('7869012345')

upload_file=wait.until(EC.invisibility_of_element_located((By.XPATH ,'//input[@multiple="multiple"]')))
upload_file.send_keys(r'C:\Users\Dell\Downloads\photo01.jpg')


country_DD=wait.until(EC.visibility_of_element_located((By.NAME,'sgender')))
dropdown=Select(country_DD)
dropdown.select_by_value('female')

YOE=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@value="above 7"]')))
YOE.click()

Skills=wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//label[@for="skills"]/following-sibling::input')))
for skill in Skills:
    if skill.get_attribute('value')=="automationtesting" or  skill.get_attribute('value')=="java" or skill.get_attribute("value")=="API":
        skill.click()

tool=wait.until(EC.visibility_of_element_located((By.ID,'tools')))
tools=Select(tool)
tool.select_by_visible_text('Selenium')

submit=wait.until(EC.element_to_be_clickable((By.ID,'submit')))
submit.click()






driver.quit()
