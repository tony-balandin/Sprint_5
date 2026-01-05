from selenium.webdriver.common.by import By


class ProfilePageLocators:
    """Локаторы страницы профиля."""

    # Маркер, что профиль открыт
    PROFILE_TITLE = (By.XPATH, "//*[@id='root']/div/div[2]/form/div[1]/h1")

    # Блок "Мои объявления"
    MY_ADS_TITLE = (By.XPATH, "//*[@id='root']/div/div[2]/div[4]/h1")
    MY_ADS_GRID_AND_PAGINATION = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[4]/div/div[2]",
    )

    # Карточки/заголовки объявлений в сетке
    MY_AD_CARD = (By.XPATH, "//*[@id='root']/div/div[2]/div[4]/div/div[1]//h2")

    # Пагинация
    PAGINATION_SHELL = (By.XPATH, "//*[@id='root']/div/div[2]/div[4]/div/div[2]")
    PAGINATION_STATUS = (By.XPATH, "//*[@id='root']/div/div[2]/div[4]/div/div[2]/p")
    PAGINATION_PREV = (By.XPATH, "//*[@id='root']/div/div[2]/div[4]/div/div[2]/button[1]")
    PAGINATION_NEXT = (By.XPATH, "//*[@id='root']/div/div[2]/div[4]/div/div[2]/button[2]")

    @staticmethod
    def my_ad_title(ad_title: str):
        """Заголовок конкретного объявления в профиле (по тексту)."""
        return (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div[4]/div/div[1]"
            f"//h2[normalize-space()='{ad_title}']",
        )
