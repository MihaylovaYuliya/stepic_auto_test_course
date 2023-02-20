from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд
browser.get("http://suninjuly.github.io/cats.html")
browser.find_element(By.ID, "button")