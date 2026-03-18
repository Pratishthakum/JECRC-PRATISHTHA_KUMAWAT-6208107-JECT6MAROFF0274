## Task 1
### Link Text & Partial Link Text
# 1. Go to https://the-internet.herokuapp.com/
# 2. Find the "Checkboxes" link using LINK_TEXT
# 3. Find the "Drag and Drop" link using PARTIAL_LINK_TEXT
# 4. Find how many <li> (list item) elements are on the page using find_elements and TAG_NAME. Print the count.
# 5. Navigate to https://the-internet.herokuapp.com/tables
# 6. Write an XPath to find the "Web Site" (td) for the person with email "jdoe@hotmail.com" in table 1 (Hint: Use text() and ancestor/following sibling or preceding-sibling).
# 7. Write an XPath to find the Delete link (a) for the person with Last Name "Bach" in table 1.
# 8. Write an XPath to find the second table `(<table>)` on the page using indexing.
# 9. Write an XPath to find the cell containing "$100.00" in table 2. Find its parent <tr> element.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
sleep(2)

checkboxes = driver.find_element(By.LINK_TEXT,'Checkboxes')
drag_and_drop = driver.find_element(By.PARTIAL_LINK_TEXT,'Drag')
Total_li = driver.find_elements(By.TAG_NAME,'li')
print(f'The Total list item elements are: {len(Total_li)}')
driver.get('https://the-internet.herokuapp.com/tables')
joe_web_site = driver.find_element(By.XPATH,'//td[text()="jdoe@hotmail.com"]/following-sibling::td[2]')
bach_delete_lnk = driver.find_element(By.XPATH,'//td[text()="Bach"]/following-sibling::td/a[2]')
second_table = driver.find_element(By.XPATH,'//table[2]')
tr_element = driver.find_element(By.XPATH,'//table[2]/descendant::tr[4]/td[4]')
driver.quit()