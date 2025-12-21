from selenium.webdriver.common.by import By


class AuthLocators:
    POPUP = (By.CSS_SELECTOR, "form[class^='popUp_shell__']")

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")

    LOGIN_SUBMIT_BTN = (By.XPATH, "//button[@type='submit' and normalize-space()='Войти']")
    GO_TO_REGISTER_BTN = (By.XPATH, "//button[@type='button' and normalize-space()='Нет аккаунта']")

    REG_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    REG_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    REG_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='submitPassword']")

    REGISTER_SUBMIT_BTN = (By.XPATH, "//button[@type='submit' and normalize-space()='Создать аккаунт']")
    GO_TO_LOGIN_BTN = (By.XPATH, "//button[@type='button' and normalize-space()='Уже есть аккаунт']")

    INPUT_ERROR_BLOCK = (By.CSS_SELECTOR, "div[class^='input_inputError__']")
    ERROR_TEXT = (By.XPATH, "//*[contains(@class,'input_span') and normalize-space()='Ошибка']")