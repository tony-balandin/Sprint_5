from selenium.webdriver.support import expected_conditions as EC

from locators.main_locators import MainLocators
from locators.auth_locators import AuthLocators


def open_auth_popup(driver, wait, base_url: str):
    driver.get(base_url)

    wait.until(EC.element_to_be_clickable(MainLocators.AUTH_BTN)).click()
    wait.until(EC.visibility_of_element_located(AuthLocators.POPUP))

    # на случай чтобы поля точно были доступны
    wait.until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))


def register_user(driver, wait, base_url: str, email: str, password: str):
    open_auth_popup(driver, wait, base_url)

    wait.until(EC.element_to_be_clickable(AuthLocators.GO_TO_REGISTER_BTN)).click()

    wait.until(EC.visibility_of_element_located(AuthLocators.REG_EMAIL_INPUT)).send_keys(email)
    wait.until(EC.visibility_of_element_located(AuthLocators.REG_PASSWORD_INPUT)).send_keys(password)
    wait.until(EC.visibility_of_element_located(AuthLocators.REG_CONFIRM_PASSWORD_INPUT)).send_keys(password)

    wait.until(EC.element_to_be_clickable(AuthLocators.REGISTER_SUBMIT_BTN)).click()

    # ждём, что попап закрылся
    wait.until(EC.invisibility_of_element_located(AuthLocators.POPUP))

    # маркер успешной авторизации
    wait.until(EC.visibility_of_element_located(MainLocators.LOGOUT_BTN))


def login_user(driver, wait, base_url: str, email: str, password: str):
    open_auth_popup(driver, wait, base_url)

    wait.until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)).send_keys(email)
    wait.until(EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT)).send_keys(password)

    wait.until(EC.element_to_be_clickable(AuthLocators.LOGIN_SUBMIT_BTN)).click()

    wait.until(EC.invisibility_of_element_located(AuthLocators.POPUP))
    wait.until(EC.visibility_of_element_located(MainLocators.LOGOUT_BTN))