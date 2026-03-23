from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()



# Name=driver.find_element(By.ID ,'name')
# Name.send_keys("Pratishtha")
# sleep(2)
#
# Email=driver.find_element(By.ID ,'email')
# Email.send_keys("pratishtha123@gmail.com")
# sleep(2)
#
# Phone=driver.find_element(By.ID ,'phone')
# Phone.send_keys("123456789")
# sleep(1)
#
# Address=driver.find_element(By.ID ,'textarea')
# Address.send_keys("18, Maharaja Colony ,teen dukan,sikar road ,jaipur")
# sleep(1)
#
#
# Gender=driver.find_element(By.ID,'female').click()
# sleep(1)
#
# checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
#
# for cb in checkboxes[:7]:
#     cb.click()
#     sleep(1)
#
# for cb in checkboxes[6:0:-1]:
#     cb.click()
#     sleep(1)
#
#
# drop_down_btn = driver.find_element(By.ID,'country')
# dropdown=Select(drop_down_btn)
# dropdown.select_by_value("usa")
# sleep(1)
# dropdown.select_by_index(1)
# sleep(1)
#
# dropdown.select_by_visible_text("India")
# sleep(1)


multi_drop = driver.find_element(By.ID,'colors')
select=Select(multi_drop)
if select.is_multiple:
    select.select_by_index(1)
    select.select_by_visible_text("Green")

print("before deselected:", [i.text for i in select.all_selected_options])
sleep(3)

select.deselect_by_visible_text("Green")
print("after deselected:", [i.text for i in select.all_selected_options])
sleep(3)




driver.quit()