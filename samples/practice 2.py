from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://omayo.blogspot.com/")
time.sleep(3)
driver.find_element(By.ID,"ta1").clear()
driver.find_element(By.ID,"ta1").send_keys("srikanth")
time.sleep(2)
driver.close()