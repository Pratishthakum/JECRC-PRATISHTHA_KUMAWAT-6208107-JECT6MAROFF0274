#Add the songs which contain the word love/girl

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get(r'C:\Users\Dell\Downloads\playlist.html')


driver.maximize_window()

songs=driver.find_element(By.ID,'songs')
select=Select(songs)
all_songs=[i.text for i in select.options]
if select.is_multiple:
    for song in all_songs:
        if "Love" in song or "Girl" in song:
            select.select_by_visible_text(song)
            print(song)

driver.find_element(By.TAG_NAME,'button').click()

sleep(10)
driver.quit()



