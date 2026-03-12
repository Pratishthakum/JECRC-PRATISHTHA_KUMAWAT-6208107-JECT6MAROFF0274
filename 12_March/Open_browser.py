from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://supertails.com/")
sleep(3)
driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(5)
driver.quit()

driver = webdriver.Chrome()
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get("https://supertails.com/")
#sleep(3)
driver.maximize_window()
sleep(2)
driver.minimize_window()
driver.forward()
driver.back()
driver.refresh()
sleep(3)


opts=webdriver.EdgeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Edge(options=opts)

driver.get("https://supertails.com/")
#sleep(3)
driver.maximize_window()


opts=webdriver.FirefoxOptions()
opts.set_preference('detach',True)
driver = webdriver.Firefox(options=opts)

driver.get("https://supertails.com/")
#sleep(3)
driver.maximize_window()


# driver.close()
driver.quit()




opts=webdriver.EdgeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Edge(options=opts)

# driver.get("https://supertails.com/")
driver.get("https://topbrains.com/")
print(driver.title)
print(f"title of the website: {driver.title}")
#sleep(3)
driver.maximize_window()
print(driver.title)
driver.close()
driver.quit()









driver.maximize_window()
driver.quit()




driver = webdriver.Firefox()

driver.get("https://www.amazon.in/")
sleep(3)
driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(5)



driver.quit()