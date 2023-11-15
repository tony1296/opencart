from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID,"multiselect1").click()
driver.find_element(By.XPATH,"//*[@id='multiselect1']/option[1]")
time.sleep(3)
driver.close()