from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.hyrtutorials.com/p/add-padding-to-containers.html")
foll_sib1=driver.find_element(By.XPATH , '//label[text()="Email"] /following-sibling::input[1]')
print(foll_sib1)
print("following sibling found")
parent01=driver.find_element(By.XPATH , '//label[text()="Email"] /following-sibling::input[1]/parent::div')
print(parent01)
print("parent element found")

child01=driver.find_element(By.XPATH ,'//div[@class="container"]/child::input[@type="text"]')
print(child01)
print("child found")
# on the basis of contact name identify the checkbox in the table
preceding_sib01=driver.find_element(By.XPATH , '//td[text()="Maria Anders"]/preceding-sibling::td/child::input')
print(preceding_sib01)
print("preceding sibling found")

descendant01=driver.find_element(By.XPATH , '//div[@class="container"]/descendant::button')
print(descendant01)
print("descendant found")
ancestor01=driver.find_element(By.XPATH ,'//div[@class="buttons"]/ancestor::div[1]') #returns first ancestor
print(ancestor01)
print("ancestor found")
following_only=driver.find_element(By.XPATH,'//label[text()="Password"]/following::input[1]')
print(following_only)
print("first following found")
driver.quit()
