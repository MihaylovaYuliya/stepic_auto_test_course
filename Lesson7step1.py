from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.ID,"input_value")
x = x_element.text  #Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента. Например, text для данного элемента <div class="message">У вас новое сообщение.</div> вернёт строку: "У вас новое сообщение".
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