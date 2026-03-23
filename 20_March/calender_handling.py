from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')

calender1=driver.find_element(By.ID,'datepicker')
calender1.send_keys('04/01/2020',Keys.ENTER)

month='May'
date=2
year='2030'
driver.find_element(By.ID,'txtDate').click()
month_input=Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-month"]'))
month_input.select_by_visible_text(month)

year_input=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
year_input.select_by_visible_text(year)

driver.find_element(By.XPATH,f'//a[text()={date}]/parent::td').click()

sleep(10)
