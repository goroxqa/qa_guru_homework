import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Tests:
    def __init__(self, url):
        self.__url = url  # Сохраняем URL

    def get_url(self):
        return self.__url

    def get_driver(self):
        return self.__driver

    def set_driver(self, driver):
        self.__driver = driver

    full_name_locator = "userName"
    email_locator = "userEmail"
    submit_button_locator = "submit"
    result_box_locator = "output"
    cur_address_locator = "currentAddress"

    # Запуск браузера
    def set_up(self):
        self.__driver = webdriver.Chrome()
        self.get_driver().get(self.get_url())
        self.get_driver().maximize_window()
        time.sleep(3)

    # Закрытие браузера
    def teardown(self):
        self.get_driver().quit()

    def test01(self):
        try:
            self.set_up()

            full_name_field = self.get_driver().find_element(By.ID, self.full_name_locator)
            full_name_field.send_keys("Иван Иванов")

            email_field = self.get_driver().find_element(By.ID, self.email_locator)
            email_field.send_keys("ivan@example.com")

            submit_button = self.get_driver().find_element(By.ID, self.submit_button_locator)
            submit_button.click()

            time.sleep(3)

            result_box = self.get_driver().find_element(By.ID, self.result_box_locator)

            assert "Иван Иванов" in result_box.text
            print("Тест 1 успешно пройден!")

        finally:
            self.teardown()

    def test02(self):
        try:
            self.set_up()

            full_name_field = self.get_driver().find_element(By.ID, self.full_name_locator)
            full_name_field.send_keys("Иван Иванов")

            email_field = self.get_driver().find_element(By.ID, self.email_locator)
            email_field.send_keys("ivan@example.com")

            cur_address_field = self.get_driver().find_element(By.ID, self.cur_address_locator)
            cur_address_field.send_keys("СПб, ул. Ленина, д.1, кв.1")

            submit_button = self.get_driver().find_element(By.ID, self.submit_button_locator)
            submit_button.click()

            time.sleep(3)

            result_box = self.get_driver().find_element(By.ID, self.result_box_locator)

            assert "Иван Иванов" in result_box.text
            print("Тест 2 успешно пройден!")

        finally:
            self.teardown()

    def test03(self):
        try:
            self.set_up()

            full_name_field = self.get_driver().find_element(By.ID, self.full_name_locator)
            full_name_field.send_keys("Иван Иванов")

            email_field = self.get_driver().find_element(By.ID, self.email_locator)
            email_field.send_keys("ivanexample.com")  # Некорректный email

            submit_button = self.get_driver().find_element(By.ID, self.submit_button_locator)
            submit_button.click()

            time.sleep(3)

            result_box = self.get_driver().find_element(By.ID, self.result_box_locator)

            assert "Иван Иванов" in result_box.text
            print("Тест 3 успешно пройден!")

        finally:
            self.teardown()


# Запуск
url = "https://qa-guru.github.io/one-page-form/text-box.html"
test_suite = Tests(url)

test_suite.test01()
test_suite.test02()
test_suite.test03()
