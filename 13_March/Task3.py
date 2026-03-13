from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
Search_bar=driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox")
print(Search_bar)
Amazon_logo=driver.find_element(By.CSS_SELECTOR,"#nav-logo-sprites")
print(Amazon_logo)
cart=driver.find_element(By.CSS_SELECTOR,"#nav-cart")
print(cart)
sign_in=driver.find_element(By.CSS_SELECTOR,'div[id="nav-tools"] a[href*="signin"]')
print(" sign-in link")
categories = driver.find_elements(By.CSS_SELECTOR, "#nav-xshop a")
print("Total categories: ",len(categories))
for category in categories:
    print(category.text)





driver.quit()







