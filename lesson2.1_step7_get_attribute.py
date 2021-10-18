import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))

    chest = browser.find_element(By.XPATH, '//*[@id="treasure"]')
    x = chest.get_attribute('valuex')

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(calc(int(x)))

    check = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    check.click()

    robots = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    robots.click()

    button = browser.find_element(By.XPATH, '/html/body/div/form/div/div/button')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()