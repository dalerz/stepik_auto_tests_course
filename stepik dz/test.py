import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(2)

driver.get("https://tjob.alif.tj/admin/auth/login")
# set_window_size(1)
driver.set_window_size(1400, 800)
time.sleep(2)

login_form = driver.find_element("name", "email")


login_form.send_keys("testing199601@mail.ru")
time.sleep(2)

password_form = driver.find_element("name", "password")

password_form.send_keys("888859414a")
time.sleep(2)


button_element = driver.find_element(By.XPATH, '//button[@form="login-form"]')

button_element.click()
time.sleep(3)

button_element = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/div[1]/nav/div[3]/a[1]')
button_element.click()
time.sleep(5)

driver.refresh()


driver.quit()