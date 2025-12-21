from selenium.webdriver.support import expected_conditions as EC

from locators.main_locators import MainLocators
from locators.auth_locators import AuthLocators
from tests.helpers import open_auth_popup


class TestRegistration:
    def test_registration_success(self, driver, wait, base_url, unique_email, valid_password):
        open_auth_popup(driver, wait, base_url)

        wait.until(EC.element_to_be_clickable(AuthLocators.GO_TO_REGISTER_BTN)).click()

        wait.until(EC.visibility_of_element_located(AuthLocators.REG_EMAIL_INPUT)).send_keys(unique_email)
        driver.find_element(*AuthLocators.REG_PASSWORD_INPUT).send_keys(valid_password)
        driver.find_element(*AuthLocators.REG_CONFIRM_PASSWORD_INPUT).send_keys(valid_password)

        wait.until(EC.element_to_be_clickable(AuthLocators.REGISTER_SUBMIT_BTN)).click()

        wait.until(EC.visibility_of_element_located(MainLocators.AUTH_BTN))
        assert driver.find_element(*MainLocators.AUTH_BTN).is_displayed()

    def test_registration_invalid_email_shows_error(self, driver, wait, base_url):
        open_auth_popup(driver, wait, base_url)

        wait.until(EC.element_to_be_clickable(AuthLocators.GO_TO_REGISTER_BTN)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.REG_EMAIL_INPUT)).send_keys("tonybalandin")

        wait.until(EC.element_to_be_clickable(AuthLocators.REGISTER_SUBMIT_BTN)).click()

        wait.until(EC.visibility_of_element_located(AuthLocators.INPUT_ERROR_BLOCK))
        wait.until(EC.visibility_of_element_located(AuthLocators.ERROR_TEXT))

        assert driver.find_element(*AuthLocators.ERROR_TEXT).is_displayed()

    def test_registration_existing_user_shows_error(self, driver, wait, base_url, existing_user_credentials, valid_password):
        open_auth_popup(driver, wait, base_url)

        wait.until(EC.element_to_be_clickable(AuthLocators.GO_TO_REGISTER_BTN)).click()

        wait.until(EC.visibility_of_element_located(AuthLocators.REG_EMAIL_INPUT)).send_keys(existing_user_credentials["email"])
        driver.find_element(*AuthLocators.REG_PASSWORD_INPUT).send_keys(valid_password)
        driver.find_element(*AuthLocators.REG_CONFIRM_PASSWORD_INPUT).send_keys(valid_password)

        wait.until(EC.element_to_be_clickable(AuthLocators.REGISTER_SUBMIT_BTN)).click()

        wait.until(EC.visibility_of_element_located(AuthLocators.INPUT_ERROR_BLOCK))
        wait.until(EC.visibility_of_element_located(AuthLocators.ERROR_TEXT))

        assert driver.find_element(*AuthLocators.ERROR_TEXT).is_displayed()