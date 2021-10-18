import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element(By.XPATH, '//*[@id="input_value"]').text

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(calc(x))

    check_robot = browser.find_element(By.CSS_SELECTOR, '[class="form-check-label"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_robot)
    check_robot.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()

