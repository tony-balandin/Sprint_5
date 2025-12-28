from selenium.webdriver.common.by import By


class AuthPopupLocators:
    LOGIN_TITLE = (
        By.XPATH,
        "//*[self::h1 or self::h2 or self::div][contains(normalize-space(.), 'Вход') or contains(normalize-space(.), 'Login')]",
    )

    CLOSE_BTN = (
        By.XPATH,
        "//button[contains(@class, 'close') or @aria-label='Закрыть' or normalize-space(.)='×']",
    )

    LOGIN_EMAIL = (By.XPATH, "//input[@name='email' or @placeholder='Email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@name='password' or @placeholder='Пароль']")
    LOGIN_SUBMIT = (
        By.XPATH,
        "//button[contains(normalize-space(.), 'Войти') or contains(normalize-space(.), 'Login')]",
    )

    NO_ACCOUNT = (
        By.XPATH,
        "//*[self::button or self::a][contains(normalize-space(.), 'Нет аккаунта') or contains(normalize-space(.), 'Создать') or contains(normalize-space(.), 'Register')]",
    )

    REG_TITLE = (
        By.XPATH,
        "//*[self::h1 or self::h2 or self::div][contains(normalize-space(.), 'Регистрация') or contains(normalize-space(.), 'Создать аккаунт') or contains(normalize-space(.), 'Registration')]",
    )

    REG_EMAIL = (By.XPATH, "//input[@name='email' or @placeholder='Email']")
    REG_PASSWORD = (By.XPATH, "//input[@name='password' or @placeholder='Пароль']")
    REG_REPEAT_PASSWORD = (
        By.XPATH,
        "//input[@name='repeatPassword' or @placeholder='Повторите пароль']",
    )

    CREATE_ACCOUNT = (
        By.XPATH,
        "//button[contains(normalize-space(.), 'Создать аккаунт') or contains(normalize-space(.), 'Create')]",
    )

    ALREADY_HAVE_ACCOUNT = (
        By.XPATH,
        "//*[self::button or self::a][contains(normalize-space(.), 'Уже есть аккаунт') or contains(normalize-space(.), 'Войти')]",
    )

    ERROR_TEXT = (
        By.XPATH,
        "//*[normalize-space()='Ошибка']",
    )

    EMAIL_ERROR = ERROR_TEXT