from selenium.webdriver.common.by import By


class AdFormLocators:
    """Локаторы формы создания объявления."""

    NEW_AD_TITLE = (By.XPATH, "//h1[contains(@class,'createListing_title')]")

    TITLE = (
        By.XPATH,
        "//input[@name='name' and @placeholder='Название']",
    )
    DESCRIPTION = (
        By.XPATH,
        "//textarea[@name='description' and @placeholder='Описание товара']",
    )
    PRICE = (
        By.XPATH,
        "//input[@name='price' and @placeholder='Стоимость']",
    )

    # Выпадающий список категории
    CATEGORY_OPEN = (
        By.XPATH,
        "//div[contains(@class,'dropDownMenu_input')][.//input[@name='category']]//button[@type='button']",
    )
    CATEGORY_OPTIONS = (
        By.XPATH,
        "//div[contains(@class,'dropDownMenu_options') and .//button[contains(@class,'dropDownMenu_btn')]]",
    )

    @staticmethod
    def category_option(text: str):
        return (
            By.XPATH,
            f"//div[contains(@class,'dropDownMenu_options')]//button[.//span[normalize-space()='{text}']]",
        )

    # Выпадающий список города
    CITY_OPEN = (
        By.XPATH,
        "//div[contains(@class,'dropDownMenu_input')][.//input[@name='city']]//button[@type='button']",
    )
    CITY_OPTIONS = (
        By.XPATH,
        "//div[contains(@class,'dropDownMenu_options')]",
    )

    @staticmethod
    def city_option(text: str):
        return (
            By.XPATH,
            f"//div[contains(@class,'dropDownMenu_options')]//button[.//span[normalize-space()='{text}']]",
        )

    # Состояние товара (Новый / Б/У)
    CONDITION_ANY = (
        By.XPATH,
        "//fieldset//div[contains(@class,'radioUnput_input')]",
    )

    # Публикация
    PUBLISH = (
        By.XPATH,
        "//button[@type='submit' and normalize-space()='Опубликовать']",
    )
