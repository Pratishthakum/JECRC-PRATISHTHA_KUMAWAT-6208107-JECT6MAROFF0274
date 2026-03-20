from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get('https://abc.com/')
driver.maximize_window()

#explicit waits are not global - always confined to a particular element
#throws time out exception after time is up , we will not know whether element was not found /clickable and so on
#It doesnt give enough information about the error


wait_obj=WebDriverWait(driver,10)
#frequency defines that in that time duration, how many times the element is searched in the structure
#altering the polling frequency is called fluid waits

submit_button=wait_obj.until(ec.element_to_be_clickable((By.XPATH,'//button[@class="Searchlist__button"]')))
submit_button.click()

wait_obj2=WebDriverWait(driver,10,poll_frequency=2)
#frequency defines that in that time duration, how many times the element is searched in the structure
#altering the polling frequency is called fluid waits
ele=wait_obj2.until(ec.element_to_be_clickable((By.ID,'hero-items')))
ele.click()

loading=wait_obj.until(ec.invisibility_of_element_located((By.ID,'preloader-animated_svg__svg3')))
title_abc=driver.find_element(By.XPATH,'//span[text()="ABC SHOWS, SPECIALS & MORE"]')
assert 'SPECIALS' in title_abc.text, 'text not present'
print('working fine')
#will wait till these elements become invisible

driver.get('https://demoqa.com/dynamic-properties')
driver.maximize_window()
wait=WebDriverWait(driver,6)

enable_before=driver.find_element(By.ID,'enableAfter')
print(enable_before.is_enabled())

enable_button=wait.until(ec.element_to_be_clickable((By.ID,'enableAfter')))

if enable_button.is_enabled():
    enable_button.click()
    print(enable_button.text)

visible_button=wait.until(ec.visibility_of_element_located((By.ID,'visibleAfter')))
visible_button.click()

driver.quit()