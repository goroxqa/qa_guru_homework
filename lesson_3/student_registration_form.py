import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationForm:

    FIRST_NAME_LOCATOR = (By.ID, "firstName")
    LAST_NAME_LOCATOR = (By.ID, "lastName")
    EMAIL_LOCATOR = (By.ID, "userEmail")
    GENDER_MALE_LOCATOR = (By.ID, "gender-radio-1")
    GENDER_FEMALE_LOCATOR = (By.ID, "gender-radio-2")
    GENDER_OTHER_LOCATOR = (By.ID, "gender-radio-3")
    MOBILE_LOCATOR = (By.ID, "userNumber")
    DATE_OF_BIRTH_LOCATOR = (By.ID, "dateOfBirthInput")
    SUBJECTS_LOCATOR = (By.ID, "subjectsInput")
    HOBBIES_SPORT_LOCATOR = (By.ID, "hobbies-checkbox-1")
    HOBBIES_READING_LOCATOR = (By.ID, "hobbies-checkbox-2")
    HOBBIES_MUSIC_LOCATOR = (By.ID, "hobbies-checkbox-3")
    PICTURE_LOCATOR = (By.ID, "uploadPicture")
    ADDRESS_LOCATOR = (By.ID, "currentAddress")
    STATE_LOCATOR = (By.ID, "state")
    CITY_LOCATOR = (By.ID, "city")
    SUBMIT_LOCATOR = (By.ID, "submit")
    RESULT_TABLE_LOCATOR = (By.ID, "resultBody")
    CLOSE_MODAL_LOCATOR = (By.CSS_SELECTOR, "button[aria-label='Close']")
    ERROR_LOCATOR = (By.ID, "formError")
    POPUP_CLOSE_BTN = (By.XPATH, "//*[@id='fixedban']/div/div/button")

    def __init__(self):
        self.url = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)

    def set_up(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.close_popup()

    def teardown(self):
        if os.path.exists("test_image.jpg"):
            os.remove("test_image.jpg")
        self.driver.quit()

    def close_popup(self):
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Level up your automation')]")
            ))
            close_btn = self.wait.until(EC.element_to_be_clickable(self.POPUP_CLOSE_BTN))
            close_btn.click()
            time.sleep(1)
        except:
            pass

    def enter_first_name(self, value):
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys(value)

    def enter_last_name(self, value):
        self.driver.find_element(*self.LAST_NAME_LOCATOR).send_keys(value)

    def enter_email(self, value):
        self.driver.find_element(*self.EMAIL_LOCATOR).send_keys(value)

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(*self.GENDER_MALE_LOCATOR).click()
        elif gender == "Female":
            self.driver.find_element(*self.GENDER_FEMALE_LOCATOR).click()
        elif gender == "Other":
            self.driver.find_element(*self.GENDER_OTHER_LOCATOR).click()

    def enter_mobile(self, value):
        self.driver.find_element(*self.MOBILE_LOCATOR).send_keys(value)

    def select_date_of_birth(self, day, month, year):
        self.driver.find_element(*self.DATE_OF_BIRTH_LOCATOR).click()

        month_select = Select(self.driver.find_element(By.CSS_SELECTOR, "select.react-datepicker__month-select"))
        month_select.select_by_value(str(month))

        year_select = Select(self.driver.find_element(By.CSS_SELECTOR, "select.react-datepicker__year-select"))
        year_select.select_by_value(str(year))

        day_element = self.driver.find_element(By.CSS_SELECTOR, f"span[data-day='{day}']")
        day_element.click()

    def select_subjects(self, subjects):
        for subject in subjects:
            subject_input = self.driver.find_element(*self.SUBJECTS_LOCATOR)
            subject_input.click()
            subject_input.send_keys(subject)

            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, f"//div[@class='subjects-auto-complete__option' and text()='{subject}']")
                )
            ).click()

    def select_hobby(self, hobby):
        if hobby == "Sports":
            self.driver.find_element(*self.HOBBIES_SPORT_LOCATOR).click()
        elif hobby == "Reading":
            self.driver.find_element(*self.HOBBIES_READING_LOCATOR).click()
        elif hobby == "Music":
            self.driver.find_element(*self.HOBBIES_MUSIC_LOCATOR).click()

    def upload_picture(self, path):
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write("fake image data")

        abs_path = os.path.abspath(path)
        self.driver.find_element(*self.PICTURE_LOCATOR).send_keys(abs_path)

    def enter_address(self, value):
        self.driver.find_element(*self.ADDRESS_LOCATOR).send_keys(value)

    def select_state(self, state):
        state_dropdown = self.driver.find_element(*self.STATE_LOCATOR)
        state_dropdown.click()

        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{state}']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", option)
        option.click()

    def select_city(self, city):
        city_dropdown = self.driver.find_element(*self.CITY_LOCATOR)
        city_dropdown.click()

        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{city}']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", option)
        option.click()

    def select_state_and_city(self, state, city):
        self.select_state(state)
        self.select_city(city)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("document.getElementsByTagName('footer')[0].style.display='none';")

    def click_submit(self):
        submit = self.driver.find_element(*self.SUBMIT_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

    def check_error(self):
        error = self.driver.find_element(*self.ERROR_LOCATOR)
        assert error.text == "", f"Найдена ошибка: {error.text}"

    def get_result_table(self):
        return self.driver.find_element(*self.RESULT_TABLE_LOCATOR)

    def close_modal(self):
        close_btn = self.wait.until(EC.element_to_be_clickable(self.CLOSE_MODAL_LOCATOR))
        close_btn.click()

    def check_result(self, expected_data):
        result_table = self.get_result_table()
        result_text = result_table.text

        for key, value in expected_data.items():
            if key == "subjects":
                for subject in value:
                    assert subject in result_text, f"Предмет '{subject}' не найден"
            elif key == "hobbies":
                for hobby in value:
                    assert hobby in result_text, f"Хобби '{hobby}' не найдено"
            else:
                assert value in result_text, f"'{value}' не найден в таблице"


def test_full_form():
    test = TestRegistrationForm()

    data = {
        "first_name": "Alex",
        "last_name": "Smit",
        "email": "qwerty@mail.ru",
        "gender": "Male",
        "mobile": "9876543210",
        "day": "13",
        "month": "2",
        "year": "1988",
        "subjects": ["Maths", "English", "History"],
        "hobbies": ["Sports"],
        "picture": "test_image.jpg",
        "address": "450 Park Avenue, Apt 3A, New York, NY 10022",
        "state": "Uttar Pradesh",
        "city": "Lucknow"
    }

    expected = {
        "first_name": "Alex",
        "last_name": "Smit",
        "email": "qwerty@mail.ru",
        "gender": "Male",
        "mobile": "9876543210",
        "date": "13 Mar 1988",
        "subjects": ["Maths", "English", "History"],
        "hobbies": ["Sports"],
        "picture": "test_image.jpg",
        "address": "450 Park Avenue, Apt 3A, New York, NY 10022",
        "state_city": "Uttar Pradesh Lucknow"
    }

    try:
        test.set_up()

        test.enter_first_name(data["first_name"])
        test.enter_last_name(data["last_name"])
        test.enter_email(data["email"])
        test.select_gender(data["gender"])
        test.enter_mobile(data["mobile"])
        test.select_date_of_birth(data["day"], data["month"], data["year"])
        test.select_subjects(data["subjects"])

        for hobby in data["hobbies"]:
            test.select_hobby(hobby)

        test.upload_picture(data["picture"])
        test.enter_address(data["address"])
        test.scroll_to_bottom()
        test.select_state_and_city(data["state"], data["city"])

        test.click_submit()

        test.check_error()
        test.check_result(expected)

        print("Тест успешно пройден!")

    except AssertionError as error:
        print(f"Тест не пройден: {error}")
        raise
    finally:
        test.teardown()


if __name__ == "__main__":
    test_full_form()