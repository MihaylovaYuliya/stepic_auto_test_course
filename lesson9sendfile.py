from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Yukka")
input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Mikhaylova")
input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
input3.send_keys("Smolensk")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "test.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
element.send_keys(file_path)
button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()
time.sleep(60)
browser.quit()