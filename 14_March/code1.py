from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# sleep(2)
# driver.get("https://www.flipkart.com/")
# sleep(2)
# driver.get("https://www.myntra.com")
# sleep(2)
driver.get("https://www.amazon.in/")
sleep(2)

# driver.find_element(By.XPATH,'//span[text()="All"]/ancestor::div[@id="nav-main"])')
# print("element  ancestor found")

driver.find_element(By.XPATH,'//div[@id="nav-main"]/descendant::span[text()="All"]')
# driver.find_element(By.XPATH , '//div[@id="nav-logo"]/descendant::div[@id="nav-left"]')
driver.find_element(By.XPATH , '//div[@id="nav-bar-left"]/ancestor::div[@id="nav-search"]')
books = driver.find_elements(By.XPATH, "//table//tr[td[4]='300']/td[1]")


driver.quit()
