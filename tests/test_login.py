from helpers import open_main, login
from waits import wait_visible
from locators.main_page import MainPageLocators
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD


class TestLogin:
    def test_login_success(self, driver):
        open_main(driver)
        login(driver, EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD)

        text = wait_visible(driver, MainPageLocators.PROFILE_OPEN).text
        assert ('Пользователь' in text) or ('User' in text)