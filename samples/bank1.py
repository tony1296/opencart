from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/V4/index.php")
driver.find_element(By.NAME, "uid").clear()
driver.find_element(By.XPATH, "//*[@name='uid']").send_keys("mngr52535")
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "password").send_keys("YvYzUne")
driver.find_element(By.NAME, "btnLogin").click()

pop_up = driver.switch_to.alert

print(pop_up.text)

pop_up.accept()

time.sleep(5)
#if driver.title == 'Guru99 Bank Manager HomePage':
    #print("test passed")
#if driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[3]/td").is_displayed():
    #print("displayed")

driver.close()
