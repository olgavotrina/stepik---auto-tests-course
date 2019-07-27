from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = " http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.CSS_SELECTOR, '.nowrap#num1')
n1 = int(num1.get_attribute("textContent"))
print(n1)
num2 = browser.find_element(By.CSS_SELECTOR, '.nowrap#num2')
n2 = int(num2.get_attribute("textContent"))
print(n2)


sum1 = n1 + n2
print(sum1)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(sum1))


submit = browser.find_element(By.CSS_SELECTOR, '.btn')
submit.click()