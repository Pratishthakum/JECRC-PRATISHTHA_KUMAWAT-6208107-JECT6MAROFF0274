#Task 3: write a script using a loop to print the title , name and current url for all three browsers
from selenium import webdriver
from time import sleep
browsers=[webdriver.Chrome,webdriver.Edge,webdriver.Firefox]
for browser in browsers:
  driver=browser()
  driver.get("https://www.flipkart.com/")
  sleep(5)
  print(f"Title of browser : {driver.title}")
  print(f" URL for browser : {driver.current_url}")
  print(f"Name of browser : {driver.name}")
  driver.quit()

