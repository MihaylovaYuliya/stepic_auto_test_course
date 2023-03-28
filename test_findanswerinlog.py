import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                       "https://stepik.org/lesson/236896/step/1",
                                       "https://stepik.org/lesson/236897/step/1",
                                       "https://stepik.org/lesson/236898/step/1",
                                       "https://stepik.org/lesson/236899/step/1",
                                       "https://stepik.org/lesson/236903/step/1",
                                       "https://stepik.org/lesson/236904/step/1",
                                       "https://stepik.org/lesson/236905/step/1"],
								   )
def test_enter_answer(browser, links):
    browser.get(links)
    button = browser.find_element(By.CSS_SELECTOR, "a[class*='auth_login']")
    button.click()
    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys("*******")
    input2 = browser.find_element(By.ID, "id_login_password")
    input2.send_keys("*******")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    time.sleep(10)
    url = links
    browser.get(url)
    browser.implicitly_wait(20)
    element = browser.find_element(By.CSS_SELECTOR, ".textarea")
    element.clear()
    time.sleep(5)
    input3 = browser.find_element(By.CSS_SELECTOR, ".textarea")
    input3.send_keys(str(math.log(int(time.time()))))
    button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
    button.click()
    time.sleep(5)
    #button = browser.find_element(By.CSS_SELECTOR, "button[class*=again]")
    #button.click()
    #confirm = browser.switch_to.alert
    #confirm.accept()
    #time.sleep(5)
    message = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p[class*=smart-hints]"))).text
    
    assert "Correct!" in message
if __name__ == "__main__":
        pytest.main()
	
    



	
	
