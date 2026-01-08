from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы (шапка)."""

    # Кнопка "Вход и регистрация"
    AUTH_BTN = (
        By.XPATH,
        "//button[@type='button' and normalize-space()='Вход и регистрация']",
    )

    # Кнопка "Разместить объявление"
    CREATE_AD_BTN = (
        By.XPATH,
        "//button[@type='button' and normalize-space()='Разместить объявление']",
    )

    # Текст пользователя после логина
    USERNAME = (By.CSS_SELECTOR, "h3.profileText.name")

    # Кнопка-иконка профиля
    PROFILE_OPEN = (By.CSS_SELECTOR, "button.circleSmall")

    # Кнопка "Выйти"
    LOGOUT_BTN = (
        By.XPATH,
        "//button[@type='button' and normalize-space()='Выйти']",
    )
