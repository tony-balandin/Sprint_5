from selenium.webdriver.common.by import By


class MainPageLocators:
    # "Вход и регистрация" / "Войти" / "Регистрация"
    AUTH_BTN = (
        By.XPATH,
        "//*[self::a or self::button]"
        "[contains(normalize-space(.), 'Вход') or contains(normalize-space(.), 'Войти') "
        "or contains(normalize-space(.), 'Регистра') or contains(normalize-space(.), 'Зарегистр') "
        "or contains(normalize-space(.), 'Sign in') or contains(normalize-space(.), 'Log in') "
        "or contains(normalize-space(.), 'Register')]"
    )

    # "Разместить объявление"
    CREATE_AD_BTN = (
        By.XPATH,
        "//*[self::a or self::button]"
        "[contains(normalize-space(.), 'Разместить') or contains(normalize-space(.), 'объяв') "
        "or contains(normalize-space(.), 'Create') or contains(normalize-space(.), 'Post') "
        "or contains(normalize-space(.), 'Publish')]"
    )

    # Профиль
    PROFILE_OPEN = (By.CSS_SELECTOR, "h3.profileText.name")

    LOGOUT_BTN = (
        By.XPATH,
        "//*[self::a or self::button]"
        "[contains(normalize-space(.), 'Выйти') or contains(normalize-space(.), 'Logout') "
        "or contains(normalize-space(.), 'Sign out')]"
    )