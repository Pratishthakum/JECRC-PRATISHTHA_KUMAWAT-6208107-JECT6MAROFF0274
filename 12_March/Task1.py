
#Task 1 : Apply all the methods in a chrome url

from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver.get("https://www.amazon.in/")
sleep(3)


print("Title:", driver.title)

print("URL:", driver.current_url)


driver.maximize_window()
sleep(2)

driver.minimize_window()
sleep(2)


driver.maximize_window()
sleep(2)

driver.back()
driver.forward()

driver.refresh()
sleep(2)
driver.close()
driver.quit()



