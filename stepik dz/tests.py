from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    driver = webdriver.Chrome()
    driver.get(link)
    x_element = driver.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    print(x)

    y = calc(x)
    input1 = driver.find_element(By.CSS_SELECTOR, "[id='answer']")

    input1.send_keys(y)
    option1 = driver.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()
    option2 = driver.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()





    button_element = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_element.click()
    print(x)

    #
    # time.sleep(1)
    #
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # welcome_text = welcome_text_elt.text
    #
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)

    driver.quit()