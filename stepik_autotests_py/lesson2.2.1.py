from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


x_elem = browser.find_element(By.ID, 'input_value')
x = int(x_elem.get_attribute('innerHTML'))
y = calc(x)

ans = browser.find_element(By.ID, 'answer')
ans.send_keys(y)

browser.execute_script("window.scrollBy(0, 150);")

robo_check = browser.find_element(By.ID, 'robotCheckbox')
robo_check.click()

robo_radio = browser.find_element(By.ID, 'robotsRule')
robo_radio.click()

button = browser.find_element_by_css_selector('.btn')
button.click()