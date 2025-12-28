from helpers import (
    open_main,
    login,
    open_create_ad,
    fill_ad_form,
    open_profile,
    scroll_to,
    find_my_ad_in_my_ads,
)
from locators.ad_form import AdFormLocators
from locators.profile_page import ProfilePageLocators
from waits import wait_visible, wait_clickable
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD


class TestAds:
    def test_create_ad_unauthorized_shows_auth_modal(self, driver):
        open_main(driver)
        open_create_ad(driver)

        title = wait_visible(driver, AdFormLocators.NEED_AUTH_TITLE).text
        assert "авторизуйтесь" in title.lower()

    def test_create_ad_authorized_visible_in_profile(self, driver):
        open_main(driver)
        login(driver, EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD)

        open_create_ad(driver)
        wait_visible(driver, AdFormLocators.NEW_AD_TITLE)

        ad_title = "Автотест балдёжного объявления 777"

        fill_ad_form(
            driver,
            title=ad_title,
            description="Тестовое описание товара",
            price="10000000",
            category_text="Авто",
            city_text="Москва",
        )

        open_profile(driver)


        driver.execute_script("window.scrollTo(0, 0);")
        wait_visible(driver, ProfilePageLocators.MY_ADS_TITLE)
        scroll_to(driver, ProfilePageLocators.MY_ADS_TITLE)


        assert find_my_ad_in_my_ads(driver, ad_title), "Созданное объявление не найдено в профиле"