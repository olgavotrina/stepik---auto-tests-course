from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
name = browser.find_element(By.CSS_SELECTOR, ".first[placeholder='Введите имя']")
name.send_keys("blabla")
surname = browser.find_element(By.CSS_SELECTOR, ".second[placeholder='Введите фамилию']")
surname.send_keys("blabla")
email = browser.find_element(By.CSS_SELECTOR, ".third[placeholder='Введите Email']")
email.send_keys("blabla")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text