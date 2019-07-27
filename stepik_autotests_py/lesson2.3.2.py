import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

adventure = browser.find_element(By.CSS_SELECTOR, '.btn.trollface')
adventure.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_elem = browser.find_element(By.ID, 'input_value')
x = int(x_elem.get_attribute('innerHTML'))
y = calc(x)

ans = browser.find_element(By.ID, 'answer')
ans.send_keys(y)

button = browser.find_element_by_css_selector('.btn')
button.click()
