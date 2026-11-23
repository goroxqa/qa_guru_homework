from selenium import webdriver
from login_form import LoginForm
from time import sleep

# Невалидные логин и пароль
def test_invalid_login_and_password():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        driver.get("https://qa-guru.github.io/one-page-form/login.html")
        login_page = LoginForm(driver)
        login_page.login('andrei123', '123123')
        error_message = login_page.get_error_message()
        assert error_message == 'Wrong login or password'

    finally:
        driver.quit()
# Валидный логин и пароль 1
def test_valid_login():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        driver.get("https://qa-guru.github.io/one-page-form/login.html")
        login_page = LoginForm(driver)
        login_page.login('user1', 'password1')
        welcome_message = login_page.get_welcome_message()
        assert welcome_message == 'Welcome, user1!'
    finally:
        driver.quit()

# Тест выхода из профиля (кнопка logout)
def test_logout_button():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        driver.get("https://qa-guru.github.io/one-page-form/login.html")
        login_page = LoginForm(driver)
        login_page.login('user1', 'password1')
        login_page.logout()
        assert login_page.is_login_form_visible()
        sleep(2)
    finally:
        driver.quit()
