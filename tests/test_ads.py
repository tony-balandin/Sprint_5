from selenium.webdriver.support import expected_conditions as EC

from locators.main_locators import MainLocators
from locators.auth_locators import AuthLocators
from locators.ad_locators import AdLocators
from locators.profile_locators import ProfileLocators
from tests.helpers import register_user


def select_dropdown(wait, name: str, value_text: str):
    arrow = (
        AdLocators.DROPDOWN_ARROW_BY_NAME[0],
        AdLocators.DROPDOWN_ARROW_BY_NAME[1].format(name=name)
    )
    wait.until(EC.element_to_be_clickable(arrow)).click()

    option = (
        AdLocators.DROPDOWN_OPTION_BY_TEXT[0],
        AdLocators.DROPDOWN_OPTION_BY_TEXT[1].format(text=value_text)
    )
    wait.until(EC.element_to_be_clickable(option)).click()


def open_profile_and_wait(driver, wait, base_url: str):
    """
    Профиль на стендах бывает:
    - /profile
    - /#/profile
    Мы открываем по очереди и ждём якорь "Мои объявления".
    """
    # вариант 1
    driver.get(base_url.rstrip("/") + "/profile")
    try:
        wait.until(EC.visibility_of_element_located(ProfileLocators.MY_ADS_TITLE))
        return
    except Exception:
        pass

    # вариант 2 (SPA hash)
    driver.get(base_url.rstrip("/") + "/#/profile")
    wait.until(EC.visibility_of_element_located(ProfileLocators.MY_ADS_TITLE))


class TestAds:
    def test_create_ad_unauthorized_opens_auth_popup(self, driver, wait, base_url):
        driver.get(base_url)
        wait.until(EC.element_to_be_clickable(MainLocators.PLACE_AD_BTN)).click()

        wait.until(EC.visibility_of_element_located(AuthLocators.POPUP))
        assert driver.find_element(*AuthLocators.EMAIL_INPUT).is_displayed()

    def test_create_ad_authorized_success(self, driver, wait, base_url, unique_email, valid_password):
        register_user(driver, wait, base_url, unique_email, valid_password)

        wait.until(EC.element_to_be_clickable(MainLocators.PLACE_AD_BTN)).click()
        wait.until(EC.visibility_of_element_located(AdLocators.CREATE_LISTING_TITLE))

        ad_title = "Автотест: объявление"

        wait.until(EC.visibility_of_element_located(AdLocators.TITLE_INPUT)).send_keys(ad_title)
        wait.until(EC.visibility_of_element_located(AdLocators.DESCRIPTION_TEXTAREA)).send_keys("Автотест: описание товара")
        wait.until(EC.visibility_of_element_located(AdLocators.PRICE_OR_SOURCE_INPUT)).send_keys("1000")

        select_dropdown(wait, "category", "Авто")
        select_dropdown(wait, "city", "Москва")

        wait.until(EC.element_to_be_clickable(AdLocators.CONDITION_USED)).click()
        wait.until(EC.element_to_be_clickable(AdLocators.PUBLISH_BTN)).click()

        # убеждаемся, что мы всё ещё залогинены
        wait.until(EC.visibility_of_element_located(MainLocators.LOGOUT_BTN))

        # открываем профиль и проверяем объявление
        open_profile_and_wait(driver, wait, base_url)

        card = (ProfileLocators.AD_BY_TITLE[0], ProfileLocators.AD_BY_TITLE[1].format(title=ad_title))
        wait.until(EC.visibility_of_element_located(card))

        assert driver.find_element(*card).is_displayed()