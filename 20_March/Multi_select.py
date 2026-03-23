from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
driver.get(r'C:\Python\Testing\selenium\20_March\Playlist.html')


driver.maximize_window()

songs=driver.find_element(By.ID,'songs')
select=Select(songs)

if select.is_multiple:
    select.select_by_visible_text('Perfect')
    select.select_by_visible_text('Galway Girl')
    select.select_by_index(6)

list_songs=[i.text for i in select.all_selected_options]
print(list_songs)
print(f"All the options : {[i.text for i in select.options]}")
driver.find_element(By.TAG_NAME,'button').click()
sleep(10)
driver.quit()



