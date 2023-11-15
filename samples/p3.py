from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://omayo.blogspot.com/")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 1000);")
driver.find_element(By.ID,"radio1").click()
time.sleep(3)
driver.close()