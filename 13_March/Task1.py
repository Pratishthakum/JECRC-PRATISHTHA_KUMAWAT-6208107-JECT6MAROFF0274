

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
# opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)
driver.get('https://www.cricbuzz.com/')
driver.maximize_window()
sleep(5)

#By using ID locator
element1=driver.find_element(By.ID,'shosh')
print("shosh found ")
element2=driver.find_element(By.ID,'main-header')
print("header founded")

#By using name locator
NameLoc01=driver.find_element(By.NAME,'googlebot')
print("googlebot element found ")

NameLoc02=driver.find_elements(By.NAME,'robots')
print("robots element found")
print(len(NameLoc02))

NameLoc03=driver.find_element(By.NAME,'google-site-verification')
print("google-site-verification found ")

NameLoc04=driver.find_element(By.NAME,'googlefcPresent')
print("googlefcPresent element found")


#by locating using class

ClassLocator1=driver.find_element(By.CLASS_NAME,'page-wrapper')
print(" class page-wrapper found ")
# ClassLocator2=driver.find_element(By.CLASS_NAME,'GoogleActiveViewInnerContainer')
# print(" class active google inner container found")
Class_locator2=driver.find_element(By.CLASS_NAME,'grippy-host')
print("Class grippy-host found")
ClassLocator3=driver.find_elements(By.CLASS_NAME,'col-span-9')
print(f"no of elements in col-span-9 : {len(ClassLocator3)}")

#tag name locators
Tag_ele01=driver.find_element(By.TAG_NAME,'img')
print("Tag image found")
Tag_ele02=driver.find_element(By.TAG_NAME,'meta')
print("Tag meta found")
Tag_ele03=driver.find_element(By.TAG_NAME,'button')
print("Tag button found")
Tag_ele04=driver.find_elements(By.TAG_NAME,'a')
print(f"{len(Tag_ele04)} elements are present in anchor tag")

#CSS locators
CSS_Locator01=driver.find_element(By.CSS_SELECTOR,'button[class*=bg')
print("CSS element found consisting of bg class ")

CSS_Locator02=driver.find_element(By.CSS_SELECTOR,'a[href*="cricket-schedule"]')
print("CSS element found - link for cricket schedule")

#Using Xpath
Xpath01=driver.find_element(By.XPATH,'//a[@title="India vs New Zealand, Final "]')
print("Element found ")
Xpath02=driver.find_elements(By.XPATH,'span[text()="Log In"]')
print("Element found")



