from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/alerts')
driver.maximize_window()
sleep(3)

wait = WebDriverWait(driver, 10)

alert_button1=driver.find_element(By.XPATH,'//button[@id="alertButton"]').click()
driver.switch_to.alert.accept()
sleep(2)

alert_button2=driver.find_element(By.XPATH,'//button[@id="timerAlertButton"]').click()
alert=wait.until(ec.alert_is_present())
alert.accept()
sleep(2)

alert_button3=driver.find_element(By.XPATH,'//button[@id="confirmButton"]').click()
driver.switch_to.alert.accept()

sleep(2)
message=driver.find_element(By.XPATH,'(//div[@class="col-md-6"])[3]/span[2]')
assert 'Ok' in message.text, 'Error'

driver.find_element(By.ID,'confirmButton').click()
sleep(2)
alert=driver.switch_to.alert
alert.dismiss()

message02=driver.find_element(By.XPATH,'(//div[@class="col-md-6"])[3]/span[2]')
assert 'Cancel' in message02.text, 'Error'

alert_button4 = driver.find_element(By.XPATH,'//button[@id="promtButton"]').click()
alert = driver.switch_to.alert
alert.send_keys("hii from here")
alert.accept()

prompt_result=driver.find_element(By.XPATH,'//span[@id="promptResult"]')
assert "hii from here" in prompt_result.text ,'error'

driver.find_element(By.XPATH,'//button[@id="promtButton"]').click()
sleep(2)
alert=driver.switch_to.alert
alert.dismiss()


driver.quit()





