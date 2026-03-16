from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach" , True)
driver=webdriver.Chrome(options=opts)
driver.get("https://demoqa.com/radio-button")
sleep(3)
print("The title of the webpage is :", driver.title)
YesRadio_button=driver.find_element(By.XPATH ,'//input[@id="yesRadio"]')
YesRadio_button.click()
result=driver.find_element(By.XPATH,'//span[@class="text-success"]')
print(result.text)
radio_input = driver.find_element(By.ID, "yesRadio")
print("Class Attribute:", radio_input.get_attribute("class"))
print("ID Attribute:", radio_input.get_attribute("id"))
current_url=driver.current_url
print(current_url)
sleep(3)
driver.quit()



