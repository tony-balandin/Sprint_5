import uuid

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import BASE_URL
from waits import (
    wait_clickable,
    wait_visible,
    wait_present,
    wait_url_contains,
    wait_invisible,
)

from locators.main_page import MainPageLocators
from locators.auth_popup import AuthPopupLocators
from locators.ad_form import AdFormLocators
from locators.profile_page import ProfilePageLocators


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
    """Открыть форму создания объявления.

    После логина/закрытия попапа хедер может перерисовываться и даёт StaleElementReference.
    Поэтому делаем несколько попыток клика и каждый раз заново находим элемент.
    """
    driver.execute_script("window.scrollTo(0, 0);")

    candidates = [
        # После логина
        getattr(MainPageLocators, "CREATE_AD_BTN_AUTHED", None),
        # До логина
        getattr(MainPageLocators, "CREATE_AD_BTN", None),
    ]
    candidates = [c for c in candidates if c]

    last_exc = None
    for _ in range(6):
        for locator in candidates:
            try:
                elem = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException) as exc:
                last_exc = exc
                # Иногда помогает скролл наверх и повтор
                driver.execute_script("window.scrollTo(0, 0);")
                continue
            except TimeoutException as exc:
                last_exc = exc
                continue

    if last_exc:
        raise last_exc


def open_profile(driver):
    
    driver.execute_script("window.scrollTo(0, 0);")

    try:
        wait_clickable(driver, MainPageLocators.PROFILE_OPEN).click()
        wait_url_contains(driver, "/profile", timeout=10)
    except TimeoutException:
        driver.get(BASE_URL.rstrip("/") + "/profile")
        wait_url_contains(driver, "/profile", timeout=10)


    wait_visible(driver, ProfilePageLocators.PROFILE_TITLE)


def scroll_to(driver, locator):
    element = driver.find_element(*locator)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)


def wait_my_ads_block_loaded(driver):
    """Дождаться, что блок "Мои объявления" реально отрисовался.

    На стенде секция может подгружаться лениво (появляется только после скролла),
    поэтому сначала скроллим к заголовку "Мои объявления", затем ждём контейнер и
    контент (карточку или пагинацию).
    """
    wait_visible(driver, ProfilePageLocators.MY_ADS_TITLE)
    scroll_to(driver, ProfilePageLocators.MY_ADS_TITLE)


    block = wait_present(driver, ProfilePageLocators.MY_ADS_GRID_AND_PAGINATION, timeout=15)
    driver.execute_script("arguments[0].scrollIntoView(true);", block)


    WebDriverWait(driver, 15).until(
        lambda d: len(d.find_elements(*ProfilePageLocators.MY_AD_CARD)) > 0
        or len(d.find_elements(*ProfilePageLocators.PAGINATION_SHELL)) > 0
    )


def _get_total_pages_from_status(text: str) -> int:
    try:
        parts = text.split("из")
        if len(parts) != 2:
            return 1
        return int(parts[1].strip())
    except Exception:
        return 1


def find_my_ad_in_pages(driver, ad_title: str) -> bool:
    wait_my_ads_block_loaded(driver)

    if driver.find_elements(*ProfilePageLocators.my_ad_title(ad_title)):
        return True

    shells = driver.find_elements(*ProfilePageLocators.PAGINATION_SHELL)
    if not shells:
        return False

    total_pages = _get_total_pages_from_status(
        wait_visible(driver, ProfilePageLocators.PAGINATION_STATUS).text
    )

    for _ in range(max(total_pages - 1, 0)):
        next_btn = wait_visible(driver, ProfilePageLocators.PAGINATION_NEXT)

        if next_btn.get_attribute("disabled") is not None:
            break

        current_status = wait_visible(driver, ProfilePageLocators.PAGINATION_STATUS).text
        next_btn.click()

        WebDriverWait(driver, 10).until(
            lambda d: wait_visible(
                d, ProfilePageLocators.PAGINATION_STATUS
            ).text != current_status
        )

        wait_my_ads_block_loaded(driver)

        if driver.find_elements(*ProfilePageLocators.my_ad_title(ad_title)):
            return True

    return False


def find_my_ad_in_my_ads(driver, ad_title: str) -> bool:
    return find_my_ad_in_pages(driver, ad_title)


def fill_ad_form(
    driver,
    title: str,
    description: str,
    price: str,
    category_text: str,
    city_text: str,
):
    wait_visible(driver, AdFormLocators.TITLE).send_keys(title)
    wait_visible(driver, AdFormLocators.DESCRIPTION).send_keys(description)
    wait_visible(driver, AdFormLocators.PRICE).send_keys(price)

    wait_clickable(driver, AdFormLocators.CATEGORY_OPEN).click()
    wait_visible(driver, AdFormLocators.CATEGORY_OPTIONS)
    wait_clickable(driver, AdFormLocators.category_option(category_text)).click()

    wait_clickable(driver, AdFormLocators.CITY_OPEN).click()
    wait_visible(driver, AdFormLocators.CITY_OPTIONS)
    wait_clickable(driver, AdFormLocators.city_option(city_text)).click()

    try:
        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(AdFormLocators.CONDITION_ANY)
        ).click()
    except TimeoutException:
        pass

    wait_clickable(driver, AdFormLocators.PUBLISH).click()


    wait_invisible(driver, AdFormLocators.NEW_AD_TITLE, timeout=15)