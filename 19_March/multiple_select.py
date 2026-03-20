
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#you are not supposed to use implicit and explicit waits together

driver=webdriver.Chrome()
driver.get('https://demo.mobiscroll.com/select/multiple-select')
driver.maximize_window()

multi_drop=driver.find_element(By.XPATH,'//select[@id="multiple-select-select"]')
select=Select(multi_drop)

if select.is_multiple():
    select.select_by