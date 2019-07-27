import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

fname = browser.find_element(By.CSS_SELECTOR, '[name = firstname]')
fname.send_keys('Olya')

lname = browser.find_element(By.CSS_SELECTOR, '[name = lastname]')
lname.send_keys('Votrina')

email = browser.find_element(By.CSS_SELECTOR, '[name = email]')
email.send_keys('Votrina@mail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
print(current_dir)
file_path = os.path.join(current_dir, 'groove.txt')           # добавляем к этому пути имя файла

file_attach = browser.find_element(By.ID, 'file')
file_attach.send_keys(file_path)


button = browser.find_element_by_css_selector('.btn')
button.click()

