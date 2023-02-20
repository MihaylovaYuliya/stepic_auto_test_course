from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x_element = browser.find_element(By.ID,"input_value")
x = x_element.text
y = calc(x)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
input = browser.find_element(By.ID, "answer")
input.send_keys(y)
option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()
input = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", input) # так как кнопка выбора перекрыта футером пишем скрипт для прокрутки вниз
option2 = browser.find_element(By.ID, "robotsRule")
option2.click()
button = browser.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(120)
browser.quit