from selenium.webdriver.support import expected_conditions as EC

from locators.main_locators import MainLocators
from tests.helpers import register_user, login_user


class TestLogin:
    def test_login_success(self, driver, wait, base_url, unique_email, valid_password):
        # создаём пользователя
        register_user(driver, wait, base_url, unique_email, valid_password)

        # гарантированно выходим
        wait.until(EC.element_to_be_clickable(MainLocators.LOGOUT_BTN)).click()
        wait.until(EC.visibility_of_element_located(MainLocators.AUTH_BTN))

        # логинимся теми же данными
        login_user(driver, wait, base_url, unique_email, valid_password)

        assert driver.find_element(*MainLocators.LOGOUT_BTN).is_displayed()