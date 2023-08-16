from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(int(x))


element1 = browser.find_element(By.ID,'answer')
element1.send_keys(y)
time.sleep(2)
option1 = browser.find_element(By.ID,'robotCheckbox')
option1.click()
option2 = browser.find_element(By.ID,"robotsRule")
option2.click()
time.sleep(2)

button_element = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button_element.click()
time.sleep(5)