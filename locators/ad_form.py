from selenium.webdriver.common.by import By


class AdFormLocators:
    NEED_AUTH_TITLE = (
        By.XPATH,
        "//*[contains(normalize-space(.), 'разместить объявление') and contains(normalize-space(.), 'авториз')]",
    )

    NEW_AD_TITLE = (
        By.XPATH,
        "//h1[contains(@class,'createListing_title')]",
    )

    TITLE = (By.XPATH, "//input[@name='title' or @placeholder='Название']")
    DESCRIPTION = (By.XPATH, "//textarea")

    # Поле "Цена"
    PRICE = (By.XPATH, "//input[@name='price' or @placeholder='Стоимость']")

    # Алиас для совместимости с helpers.py
    PRICE_INPUT = PRICE

    # dropdown open buttons
    CATEGORY_OPEN = (
        By.XPATH,
        "//input[@name='category']/following-sibling::button",
    )

    CITY_OPEN = (
        By.XPATH,
        "//input[@name='city']/following-sibling::button",
    )

    # Контейнеры с кнопками-опциями выпадающего списка
    CATEGORY_OPTIONS = (By.CSS_SELECTOR, "div[class*='dropDownMenu_options']")
    CITY_OPTIONS = (By.CSS_SELECTOR, "div[class*='dropDownMenu_options']")

    # Выбор опции
    @staticmethod
    def category_option(text: str):
        return (
            By.XPATH,
            f"//div[contains(@class,'dropDownMenu_options')]//button[normalize-space(.)={text!r}]",
        )

    @staticmethod
    def city_option(text: str):
        return (
            By.XPATH,
            f"//div[contains(@class,'dropDownMenu_options')]//button[normalize-space(.)={text!r}]",
        )

    @staticmethod
    def category_button(_text: str = ""):
        return AdFormLocators.CATEGORY_OPEN

    @staticmethod
    def city_button():
        return AdFormLocators.CITY_OPEN

    FIRST_DROPDOWN_OPTION = (
        By.XPATH,
        "//div[contains(@class,'dropDownMenu_options')]//button[1]",
    )

    CONDITION_ANY = (
        By.XPATH,
        "//input[@type='radio'][1]/following-sibling::label",
    )

    PUBLISH = (
        By.XPATH,
        "//button[@type='submit']",
    )