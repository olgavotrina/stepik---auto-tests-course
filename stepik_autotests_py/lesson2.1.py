import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
# x = x_element.text
# y = calc(x)

x_treasure = browser.find_element(By.ID, 'treasure')
y = x_treasure.get_attribute('valuex')
answer = calc(y)

ans_input = browser.find_element(By.CSS_SELECTOR, '#answer')
ans_input.send_keys(answer)

check_robot = browser.find_element(By.ID, 'robotCheckbox')
check_robot.click()

radio_robot = browser.find_element(By.ID, 'robotsRule')
radio_robot.click()

submit = browser.find_element(By.CSS_SELECTOR, '.btn')
submit.click()