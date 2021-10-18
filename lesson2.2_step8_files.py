import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys('Name')

    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input2.send_keys('Last Name')

    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys('Email')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text_test.txt')

    input_file = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    input_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()