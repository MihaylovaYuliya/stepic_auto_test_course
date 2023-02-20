from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))  # ждем чтобы нажать на кнопку пока цена дома не станет 100$
#  selenium.webdriver.support.expected_conditions.text_to_be_present_in_element_value(locator, text_)		
button = browser.find_element(By.ID, "book")
button.click()
x_element = browser.find_element(By.ID,"input_value")
x = x_element.text
y = calc(x)
input = browser.find_element(By.ID, "answer")
input.send_keys(y)
button = browser.find_element(By.ID, "solve")
button.click()
time.sleep(60)
browser.quit()

