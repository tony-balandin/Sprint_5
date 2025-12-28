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

    TITLE = (By.XPATH, "//input[@name='title' or @name='name' or @placeholder='Название']")
    DESCRIPTION = (By.XPATH, "//textarea")


    PRICE = (By.XPATH, "//input[@name='price' or @placeholder='Стоимость']")


    PRICE_INPUT = PRICE


    CATEGORY_OPEN = (
        By.XPATH,
        "("
        "//input[@name='category' or @name='category_id' or @placeholder='Категория' or @aria-label='Категория']"
        "/ancestor::*[contains(@class,'dropDown') or contains(@class,'dropdown')][1]"
        "//*[self::button or @role='button'][1]"
        "|"
        "//*[contains(normalize-space(.), 'Категория')]/ancestor::*[contains(@class,'dropDown') or contains(@class,'dropdown')][1]"
        "//*[self::button or @role='button'][1]"
        ")",
    )

    CITY_OPEN = (
        By.XPATH,
        "("
        "//input[@name='city' or @name='city_id' or @placeholder='Город' or @aria-label='Город']"
        "/ancestor::*[contains(@class,'dropDown') or contains(@class,'dropdown')][1]"
        "//*[self::button or @role='button'][1]"
        "|"
        "//*[contains(normalize-space(.), 'Город')]/ancestor::*[contains(@class,'dropDown') or contains(@class,'dropdown')][1]"
        "//*[self::button or @role='button'][1]"
        ")",
    )

    CATEGORY_OPTIONS = (By.CSS_SELECTOR, "div[class*='dropDownMenu_options']")
    CITY_OPTIONS = (By.CSS_SELECTOR, "div[class*='dropDownMenu_options']")

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