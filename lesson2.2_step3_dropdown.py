import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x, y):
        return str(int(x) + int(y))

    x = browser.find_element(By.XPATH, '//*[@id="num1"]').text
    y = browser.find_element(By.XPATH, '//*[@id="num2"]').text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(calc(x, y))

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()