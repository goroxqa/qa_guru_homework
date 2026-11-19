from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginForm:
    LOGIN_LOCATOR = (By.ID, 'login-input')
    PASSWORD_LOCATOR = (By.ID, 'password-input')
    SUBMIT_BUTTON_LOCATOR = (By.ID, 'submit-button')
    ERROR_MESSAGE_LOCATOR = (By.ID, 'error-message')
    WELCOME_MESSAGE_LOCATOR = (By.ID, 'welcome-message')
    LOGOUT_BUTTON_LOCATOR = (By.ID, 'logout-button')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def fill_login(self,login):
        login_field = self.driver.find_element(*self.LOGIN_LOCATOR)
        login_field.send_keys(login)

    def fill_password(self,password):
        password_field = self.driver.find_element(*self.PASSWORD_LOCATOR)
        password_field.send_keys(password)

    def click_submit_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)
        submit_button.click()

    def click_logout_button(self):
        logout_button = self.wait.until(ec.element_to_be_clickable((self.LOGOUT_BUTTON_LOCATOR)))
        logout_button.click()

    def login(self, login, password):
        self.fill_login(login)
        self.fill_password(password)
        self.click_submit_button()

    def logout(self):
        self.click_logout_button()

    def get_error_message(self):
        error_element = self.wait.until(ec.visibility_of_element_located((self.ERROR_MESSAGE_LOCATOR)))
        return error_element.text

    def get_welcome_message(self):
        welcome_element = self.wait.until(ec.visibility_of_element_located((self.WELCOME_MESSAGE_LOCATOR)))
        return welcome_element.text

    def is_login_form_visible(self):
        login_field = self.wait.until(ec.visibility_of_element_located(self.LOGIN_LOCATOR))
        return login_field.is_displayed()

