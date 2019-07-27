from selenium import webdriver

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)

link_text = browser.find_element_by_partial_link_text("224592")
link_text.click()

input1 = browser.find_element_by_name("first_name")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector(".form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()