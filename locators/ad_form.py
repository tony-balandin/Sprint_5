from selenium.webdriver.common.by import By


class AdFormLocators:
    """Локаторы страницы создания объявления."""

    NEW_AD_TITLE = (By.XPATH, "//*[@id='root']/div/div[2]/div/h1")

    TITLE = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[2]/div[1]/div/div/input")
    DESCRIPTION = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[4]/div/textarea")
    PRICE = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[5]/div/div/input")

    # Категория
    CATEGORY_OPEN = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div[1]/button")
    CATEGORY_OPTIONS = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div[2]")

    @staticmethod
    def category_option(text: str):
        return (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div[2]//button[contains(normalize-space(.), %s)]"
            % repr(text),
        )

    # Город
    CITY_OPEN = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[3]/div[1]/button")
    CITY_OPTIONS = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[3]/div[2]")

    @staticmethod
    def city_option(text: str):
        return (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/form/div[3]/div[2]//button[contains(normalize-space(.), %s)]"
            % repr(text),
        )

    # Состояние товара
    CONDITION_TITLE = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/fieldset/h3")
    CONDITION_NEW = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/fieldset/div/div[1]/div")
    CONDITION_USED = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/fieldset/div/div[2]/div")

    # Для обратной совместимости с helpers.py
    CONDITION_ANY = CONDITION_NEW

    # Публикация
    PUBLISH = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/button")
