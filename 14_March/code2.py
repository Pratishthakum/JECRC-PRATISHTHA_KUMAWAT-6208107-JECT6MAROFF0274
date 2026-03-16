from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.LINK_TEXT, "Udemy Courses")
print("found the element using link_text")
driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy")
print("found element by partial link text")
ele1=driver.find_element(By.XPATH, '//td[text()="Learn Java"]/following-sibling::td[3]')
print(ele1)
ele2=driver.find_elements(By.XPATH,'//td[text()="300"]/preceding-sibling::td[3]') #find ele with price 300
for ele in ele2:
    print(ele.text)
print("found element having prices 300 found")
names=driver.find_elements(By.XPATH , '//tbody[@id="rows"]//tr/td[1]')
for name in names:
    print(name.text)




driver.quit()
