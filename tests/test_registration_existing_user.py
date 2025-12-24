from helpers import open_main, go_to_registration, register_user, EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
from locators.auth_popup import AuthPopupLocators
from waits import wait_visible


class TestRegistrationExistingUser:
    def test_register_existing_user_shows_error(self, driver):
        open_main(driver)
        go_to_registration(driver)

        wait_visible(driver, AuthPopupLocators.REG_EMAIL).send_keys(EXISTING_USER_EMAIL)
        wait_visible(driver, AuthPopupLocators.REG_PASSWORD).send_keys(EXISTING_USER_PASSWORD)
        wait_visible(driver, AuthPopupLocators.REG_REPEAT_PASSWORD).send_keys(EXISTING_USER_PASSWORD)
        wait_visible(driver, AuthPopupLocators.CREATE_ACCOUNT).click()

        wait_visible(driver, AuthPopupLocators.EMAIL_ERROR)