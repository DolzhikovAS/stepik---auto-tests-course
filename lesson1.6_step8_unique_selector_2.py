from selenium import webdriver
import time
from selenium.webdriver.common.by import By


try:
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link2)

    # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
    element1.send_keys("Мой ответ")

    element2 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
    element2.send_keys("Мой ответ")

    element3 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
    element3.send_keys("Мой ответ")

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()