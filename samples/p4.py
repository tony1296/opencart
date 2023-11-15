from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://omayo.blogspot.com/")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 1000);")
driver.find_element(By.XPATH,"//*[@id='link1']").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"What is Selenium?").click()
time.sleep(2)
driver.refresh()
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.close()