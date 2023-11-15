from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.interaction import KEY

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://omayo.blogspot.com/")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 700)")
driver.find_element(By.XPATH,"//*[@id='HTML31']/div[1]/form/input[1]").send_keys("selenium")
driver.find_element(By.XPATH,"//*[@id='HTML31']/div[1]/form/input[2]").send_keys("python")
driver.find_element(By.XPATH,"//*[@value='LogIn']").click()
time.sleep(5)
driver.close()