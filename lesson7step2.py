from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/get_attribute.html"    #Открыть страницу http://suninjuly.github.io/get_attribute.html.
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.ID, "treasure")       #Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
x = x_element.get_attribute("valuex")                     #Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
y = calc(x)
input = browser.find_element(By.ID, "answer")
input.send_keys(y)
option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()
option2 = browser.find_element(By.ID, "robotsRule")
option2.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
button.click()
time.sleep(30)
browser.quit()