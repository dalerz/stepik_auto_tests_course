import unittest
from selenium import webdriver


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        # Находим поля для ввода
        first_name = self.browser.find_element_by_css_selector(".first_block .first")
        last_name = self.browser.find_element_by_css_selector(".first_block .second")
        email = self.browser.find_element_by_css_selector(".first_block .third")

        # Заполняем поля
        first_name.send_keys("John")
        last_name.send_keys("Doe")
        email.send_keys("john@example.com")

        # Отправляем форму
        self.browser.find_element_by_css_selector("button.btn").click()

        # Проверяем, что есть сообщение об успешной регистрации
        welcome_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        # Находим поля для ввода
        first_name = self.browser.find_element_by_css_selector(".first_block .first")
        last_name = self.browser.find_element_by_css_selector(".first_block .second")
        email = self.browser.find_element_by_css_selector(".first_block .third")

        # Заполняем поля
        first_name.send_keys("John")
        last_name.send_keys("Doe")
        email.send_keys("john@example.com")

        # Отправляем форму
        self.browser.find_element_by_css_selector("button.btn").click()

        # Проверяем, что есть сообщение об успешной регистрации
        welcome_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
