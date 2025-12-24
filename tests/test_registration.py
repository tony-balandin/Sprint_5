from helpers import open_main, register_user, go_to_registration, generate_email
from waits import wait_visible, wait_clickable
from locators.main_page import MainPageLocators
from locators.auth_popup import AuthPopupLocators


class TestRegistration:
    def test_register_success(self, driver):
        open_main(driver)

        email = generate_email()
        password = "Qwerty123!"

        register_user(driver, email, password)

        text = wait_visible(driver, MainPageLocators.PROFILE_OPEN).text
        assert ('Пользователь' in text) or ('User' in text)

    def test_register_email_wrong_mask(self, driver):
        open_main(driver)
        go_to_registration(driver)

        wait_visible(driver, AuthPopupLocators.REG_EMAIL).send_keys("not-email")
        wait_clickable(driver, AuthPopupLocators.CREATE_ACCOUNT).click()

        error = wait_visible(driver, AuthPopupLocators.ERROR_TEXT).text
        assert error == "Ошибка"