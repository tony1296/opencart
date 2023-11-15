from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://omayo.blogspot.com/")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 500)")
element = driver.find_element(By.ID,"drop1")

options = Select(element)
options.select_by_visible_text("doc 1")
options.select_by_index(2)
options.select_by_value("mno")
time.sleep(5)
print(options.first_selected_option.text)
driver.close()