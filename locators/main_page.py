from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы."""

    # Кнопка "Вход и регистрация"
    AUTH_BTN = (By.XPATH, "/html/body/div/div/div[1]/div/button[1]")

    # Кнопка "Разместить объявление" (до авторизации)
    CREATE_AD_BTN = (By.XPATH, "/html/body/div/div/div[1]/div/button[2]")

    # Кнопка "Разместить объявление" (после авторизации)
    CREATE_AD_BTN_AUTHED = (By.XPATH, "//*[@id='root']/div/div[1]/div/button")

    # Имя пользователя после успешного логина
    USERNAME = (By.XPATH, "/html/body/div/div/div[1]/div/div[1]/div/h3")

    # Кнопка-иконка профиля
    PROFILE_OPEN = (By.XPATH, "//*[@id='root']/div/div[1]/div/div[1]/button")

    # Кнопка "Выйти" (в раскрытом меню профиля)
    LOGOUT_BTN = (By.XPATH, "//*[@id='root']/div/div[1]/div/div[1]/div/button")
