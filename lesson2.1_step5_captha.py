import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    field = browser.find_element(By.XPATH, '//*[@id="answer"]')
    field.send_keys(y)

    check = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    check.click()

    robots = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    robots.click()

    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
