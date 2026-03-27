from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(3)
#to the bottom of the page
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(3)

#to the origin of the page
driver.execute_script('window.scrollTo(0,0);')
sleep(3)

#scrollTo always positive  ----> start from 0,0 if we give negative value it will consider 0


#using scroll by

driver.execute_script('window.scrollBy(0,500);') #scroll 500 px down
sleep(3)
driver.execute_script('window.scrollBy(0,-200);')#scrolling up 200 px from 500 px
sleep(5)


#scrolling to element
ele=driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"]/descendant::img)[3]')
click_ele=driver.execute_script('arguments[0].scrollIntoView();',ele)
sleep(3)

#clicking

click_ele2=driver.find_element(By.XPATH,'(//div[text()="Join Pinterest"])[1]')
driver.execute_script('argument[0].click();',click_ele)
sleep(3)






















