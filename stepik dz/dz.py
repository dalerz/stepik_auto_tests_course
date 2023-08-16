from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

link = str("http://suninjuly.github.io/file_input.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.TAG_NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//body/div[1]/form[1]/div[1]/input[3]")
    input3.send_keys("ifif@jnfdk.re")
    element4 = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test1.txt')
    element4.send_keys(file_path)
    # input4 = browser.find_element(By.CSS_SELECTOR, ".form-control.first[placeholder='Input your phone:']")
    # input4.send_keys("8947362547")
    # input5 = browser.find_element(By.CSS_SELECTOR, ".form-control.second[placeholder='Input your address:'")
    # input5.send_keys("voronezh")

    button = browser.find_element(By.XPATH, "//button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла