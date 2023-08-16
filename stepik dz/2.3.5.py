from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button_element1 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button_element1.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# alert = browser.switch_to.alert
# alert.accept()

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(calc(int(x)))
time.sleep(2)

button_element2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button_element2.click()
print(browser.switch_to.alert.text.split(': ')[-1])
time.sleep(3)