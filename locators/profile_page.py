from selenium.webdriver.common.by import By


class ProfilePageLocators:
    """Локаторы страницы профиля."""

    # Маркер открытия профиля
    PROFILE_TITLE = (
        By.XPATH,
        "//h1[contains(@class,'h1') and normalize-space()='Мой профиль']",
    )

    # Заголовок секции
    MY_ADS_TITLE = (
        By.XPATH,
        "//h1[contains(@class,'h1') and normalize-space()='Мои объявления']",
    )

    # Общий контейнер сетки и пагинации
    MY_ADS_GRID_AND_PAGINATION = (
        By.XPATH,
        "//div[contains(@class,'profilePage_gridAndPaginaton')]",
    )

    # Заголовок карточки объявления
    MY_AD_CARD = (
        By.XPATH,
        "//div[contains(@class,'card')]//h2[contains(@class,'h2')]",
    )

    # Пагинация
    PAGINATION_SHELL = (By.XPATH, "//div[contains(@class,'pagination_shell')]")
    PAGINATION_STATUS = (
        By.XPATH,
        "//div[contains(@class,'pagination_shell')]//p[contains(@class,'spanGlobal')]",
    )
    PAGINATION_PREV = (
        By.XPATH,
        "//div[contains(@class,'pagination_shell')]//button[contains(@class,'arrowButton--left')]",
    )
    PAGINATION_NEXT = (
        By.XPATH,
        "//div[contains(@class,'pagination_shell')]//button[contains(@class,'arrowButton--right')]",
    )

    @staticmethod
    def my_ad_title(text: str):
        return (
            By.XPATH,
            f"//div[contains(@class,'card')]//h2[contains(@class,'h2') and normalize-space()='{text}']",
        )
