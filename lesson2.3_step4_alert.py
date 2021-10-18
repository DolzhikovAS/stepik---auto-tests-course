import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text

    browser.find_element(By.TAG_NAME, 'input').send_keys(calc(x))

    browser.find_element(By.TAG_NAME, 'button').click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()