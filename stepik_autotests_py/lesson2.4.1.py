import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

book = browser.find_element(By.ID, 'book')
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR'))


book = browser.find_element(By.ID, 'book')
book.click()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


x_elem = browser.find_element(By.ID, 'input_value')
x = int(x_elem.get_attribute('innerHTML'))
print(x)
y = calc(x)

ans = browser.find_element(By.ID, 'answer')
ans.send_keys(y)

button = browser.find_element(By.ID, 'solve')
button.click()
