import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# test_1 (успех)
driver = webdriver.Chrome()

try:
    # 2. Открытие страницы
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие

    # 3. Поиск элементов и заполнение полей
    # Находим поле Full Name по его ID и вводим текст
    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("Иван Иванов")

    # Находим поле Email по его ID и вводим текст
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("ivan@example.com")

    # Находим кнопку Submit по ее ID и кликаем
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 4. Проверка результата
    time.sleep(5)  # Пауза, чтобы увидеть результат отправки

    # Находим блок с отправленными данными
    result_box = driver.find_element(By.ID, "output")

    # Проверяем, что в блоке результата появился введенный текст
    assert "Иван Иванов" in result_box.text
    print("Тест 1 успешно пройден!")

finally:
    # 5. Закрытие браузера в любом случае
    driver.quit()

# test_2 (добавление поля Current Address)
driver = webdriver.Chrome()

try:
    # 2. Открытие страницы
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие

    # 3. Поиск элементов и заполнение полей
    # Находим поле Full Name по его ID и вводим текст
    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("Иван Иванов")

    # Находим поле Email по его ID и вводим текст
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("ivan@example.com")

    # Находим поле Current Address по его ID и вводим текст
    cur_address_field = driver.find_element(By.ID, "currentAddress")
    cur_address_field.send_keys("СПб, ул. Ленина, д.1, кв.1")

    # Находим кнопку Submit по ее ID и кликаем
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 4. Проверка результата
    time.sleep(5)  # Пауза, чтобы увидеть результат отправки

    # Находим блок с отправленными данными
    result_box = driver.find_element(By.ID, "output")

    # Проверяем, что в блоке результата появился введенный текст
    assert "Иван Иванов" in result_box.text
    print("Тест 2 успешно пройден!")

finally:
    # 5. Закрытие браузера в любом случае
    driver.quit()

# test_3 (добавление поля Permanent Address)
driver = webdriver.Chrome()

try:
    # 2. Открытие страницы
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие

    # 3. Поиск элементов и заполнение полей
    # Находим поле Full Name по его ID и вводим текст
    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("Иван Иванов")

    # Находим поле Email по его ID и вводим текст
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("ivan@example.com")

    # Находим поле Permanent Address по его ID и вводим текст
    per_address_field = driver.find_element(By.ID, "permanentAddress")
    per_address_field.send_keys("Улица Петрова, д.3, кв.55")

    # Находим кнопку Submit по ее ID и кликаем
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 4. Проверка результата
    time.sleep(5)  # Пауза, чтобы увидеть результат отправки

    # Находим блок с отправленными данными
    result_box = driver.find_element(By.ID, "output")

    # Проверяем, что в блоке результата появился введенный текст
    assert "Улица Петрова" in result_box.text
    print("Тест 3 успешно пройден!")

finally:
    # 5. Закрытие браузера в любом случае
    driver.quit()

# test_4 (некорректная почта)
driver = webdriver.Chrome()

try:
    # 2. Открытие страницы
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие

    # 3. Поиск элементов и заполнение полей
    # Находим поле Full Name по его ID и вводим текст
    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("Иван Иванов")

    # Находим поле Email по его ID и вводим текст
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("ivanexample.com")


    # Находим кнопку Submit по ее ID и кликаем
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 4. Проверка результата
    time.sleep(5)  # Пауза, чтобы увидеть результат отправки

    # 5. Получаем текст подсказки
    email_field = driver.find_element(By.CSS_SELECTOR, "input[type='email']")

    validation_message = driver.execute_script("return arguments[0].validationMessage", email_field)
    # Проверяем текст
    assert 'Адрес электронной почты должен содержать символ "@". В адресе "ivanexample.com" отсутствует символ "@".' in validation_message
    print("Тест 4 успешно пройден!")

finally:
    # 5. Закрытие браузера в любом случае
    driver.quit()
