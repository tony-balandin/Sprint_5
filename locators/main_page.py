from selenium.webdriver.common.by import By


class MainPageLocators:

    AUTH_BTN = (
        By.XPATH,
        "//*[self::a or self::button]"
        "[contains(normalize-space(.), 'Вход') or contains(normalize-space(.), 'Войти') "
        "or contains(normalize-space(.), 'Регистра') or contains(normalize-space(.), 'Зарегистр') "
        "or contains(normalize-space(.), 'Sign in') or contains(normalize-space(.), 'Log in') "
        "or contains(normalize-space(.), 'Register')]"
    )


    CREATE_AD_BTN = (
        By.XPATH,
        "//*[self::a or self::button]"
        "[contains(normalize-space(.), 'Разместить') or contains(normalize-space(.), 'объяв') "
        "or contains(normalize-space(.), 'Create') or contains(normalize-space(.), 'Post') "
        "or contains(normalize-space(.), 'Publish')]"
    )


    PROFILE_OPEN = (
        By.XPATH,
        "(//h3[contains(normalize-space(.), 'User') or contains(normalize-space(.), 'Пользователь')]/ancestor::div[1]/preceding-sibling::button"
        " | //h3[contains(normalize-space(.), 'User') or contains(normalize-space(.), 'Пользователь')]/ancestor::div[1]/following-sibling::button)[1]"
    )


    USERNAME = (
        By.XPATH,
        "//h3[contains(normalize-space(.), 'User') or contains(normalize-space(.), 'Пользователь')]"
    )

    LOGOUT_BTN = (
        By.XPATH,
        "//*[self::a or self::button]"
        "[contains(normalize-space(.), 'Выйти') or contains(normalize-space(.), 'Logout') "
        "or contains(normalize-space(.), 'Sign out')]"
    )