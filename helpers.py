import uuid

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import BASE_URL
from waits import wait_clickable, wait_visible
from locators.main_page import MainPageLocators
from locators.auth_popup import AuthPopupLocators
from locators.ad_form import AdFormLocators
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD


def generate_email() -> str:
    return f"tonybalandin+{uuid.uuid4().hex[:10]}@example.com"


def open_main(driver):
    driver.get(BASE_URL)


def open_auth_popup(driver):
    wait_clickable(driver, MainPageLocators.AUTH_BTN).click()


def go_to_registration(driver):
    open_auth_popup(driver)
    wait_clickable(driver, AuthPopupLocators.NO_ACCOUNT).click()
    wait_visible(driver, AuthPopupLocators.REG_TITLE)


def register_user(driver, email: str, password: str):
    go_to_registration(driver)
    wait_visible(driver, AuthPopupLocators.REG_EMAIL).send_keys(email)
    wait_visible(driver, AuthPopupLocators.REG_PASSWORD).send_keys(password)
    wait_visible(driver, AuthPopupLocators.REG_REPEAT_PASSWORD).send_keys(password)
    wait_clickable(driver, AuthPopupLocators.CREATE_ACCOUNT).click()


def login(driver, email: str, password: str):
    open_auth_popup(driver)
    wait_visible(driver, AuthPopupLocators.LOGIN_EMAIL).send_keys(email)
    wait_visible(driver, AuthPopupLocators.LOGIN_PASSWORD).send_keys(password)
    wait_clickable(driver, AuthPopupLocators.LOGIN_SUBMIT).click()


def open_create_ad(driver):
    for _ in range(3):
        try:
            wait_clickable(driver, MainPageLocators.CREATE_AD_BTN).click()
            return
        except StaleElementReferenceException:
            continue


from urls import BASE_URL


def open_profile(driver):
    from urls import BASE_URL

    driver.get(BASE_URL.rstrip("/") + "/profile")


def fill_ad_form(driver, title: str, description: str, price: str, category_text: str, city_text: str):
    wait_visible(driver, AdFormLocators.TITLE).send_keys(title)
    wait_visible(driver, AdFormLocators.DESCRIPTION).send_keys(description)
    wait_visible(driver, AdFormLocators.PRICE).send_keys(price)

    # Категория
    wait_clickable(driver, AdFormLocators.CATEGORY_OPEN).click()
    wait_visible(driver, AdFormLocators.CATEGORY_OPTIONS)
    wait_clickable(driver, AdFormLocators.category_option(category_text)).click()

    # Город
    wait_clickable(driver, AdFormLocators.CITY_OPEN).click()
    wait_visible(driver, AdFormLocators.CITY_OPTIONS)
    wait_clickable(driver, AdFormLocators.city_option(city_text)).click()

    # Состояние товара
    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable(AdFormLocators.CONDITION_ANY)).click()
    except TimeoutException:
        pass

    wait_clickable(driver, AdFormLocators.PUBLISH).click()