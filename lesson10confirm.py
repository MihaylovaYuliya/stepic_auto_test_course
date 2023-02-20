from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()
confirm = browser.switch_to.alert    #нажимаем кнопку подтверждения в выпадающем окне браузера
confirm.accept()
x_element = browser.find_element(By.ID,"input_value")
x = x_element.text
y = calc(x)
input = browser.find_element(By.ID, "answer")
input.send_keys(y)
button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button.click()
time.sleep(60)
browser.quit()
