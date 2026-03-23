# Task:2 Print all the songs of the fav artists

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach' , True)


driver.get(r'C:\Users\Dell\Downloads\playlist.html')
driver.maximize_window()
songs_list=driver.find_element(By.ID,'songs')
select=Select(songs_list)

for song in select.options:
    print(song.text)

fav_artist=driver.find_elements(By.XPATH , '//optgroup[@label="Justin"]/option')
if select.is_multiple:

    for artist in fav_artist:
        select.select_by_visible_text(artist.text)
        print(artist.text)


button=driver.find_element(By.XPATH, '//button')
driver.quit()





