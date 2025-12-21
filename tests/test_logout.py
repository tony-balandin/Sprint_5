from selenium.webdriver.support import expected_conditions as EC

from locators.main_locators import MainLocators
from tests.helpers import register_user


class TestLogout:
    def test_logout_success(self, driver, wait, base_url, unique_email, valid_password):
        register_user(driver, wait, base_url, unique_email, valid_password)

        wait.until(EC.element_to_be_clickable(MainLocators.LOGOUT_BTN)).click()

        wait.until(EC.visibility_of_element_located(MainLocators.AUTH_BTN))
        assert driver.find_element(*MainLocators.AUTH_BTN).is_displayed()