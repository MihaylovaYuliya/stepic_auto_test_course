from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)
x = browser.find_element(By.ID, "num1")
y = browser.find_element(By.ID, "num2")
x = int(x.text)
y = int(y.text)
sum = (x + y)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(sum))

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(60)
browser.quit()