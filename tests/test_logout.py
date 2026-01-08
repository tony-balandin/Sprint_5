from helpers import open_main, login
from waits import wait_clickable, wait_visible, wait_invisible
from locators.main_page import MainPageLocators
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD


class TestLogout:
    def test_logout_success(self, driver):
        open_main(driver)
        login(driver, EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD)

        wait_clickable(driver, MainPageLocators.LOGOUT_BTN).click()

        wait_invisible(driver, MainPageLocators.PROFILE_OPEN)

        btn_text = wait_visible(driver, MainPageLocators.AUTH_BTN).text
        assert ('Вход' in btn_text) or ('Sign' in btn_text) or ('Log' in btn_text)