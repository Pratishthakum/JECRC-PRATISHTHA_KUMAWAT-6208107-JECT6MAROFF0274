from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in/')
driver.maximize_window()
wait=WebDriverWait(driver,7)

search_box=wait.until(ec.element_to_be_clickable((By.ID,'twotabsearchtextbox')))
search_box.send_keys('Shoes')

option_04=wait.until(ec.visibility_of_element_located((By.XPATH,'//div[@class="left-pane-results-container"]//div[4]')))
option_04.click()

sort_but=wait.until(ec.visibility_of_element_located((By.XPATH,'//span[@class="a-button-text a-declarative"]')))
sort_but.click()
sort_option=wait.until(ec.visibility_of_element_located((By.ID,'s-result-sort-select_4')))
sort_option.click()
shipping_checkbox=wait.until(ec.visibility_of_element_located((By.XPATH,'//li[@id="p_n_free_shipping_eligible/205563695031"]/descendant::i')))
shipping_checkbox.click()
firstImg_name=wait.until(ec.visibility_of_element_located((By.XPATH,'//div[@class="a-section a-spacing-base desktop-grid-content-view"]/descendant::h2[2]/span')))
print(f"Name of the product: {firstImg_name.text}")
firstImg_price=wait.until(ec.visibility_of_element_located((By.XPATH,'//div[@class="a-section a-spacing-base desktop-grid-content-view"]/descendant::a[3]/span')))
print(f"Price of product: {firstImg_price.text}")