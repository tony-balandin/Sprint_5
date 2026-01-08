from selenium.webdriver.common.by import By


class AuthPopupLocators:
    """Локаторы попапа авторизации/регистрации.

    В проекте попап один, меняется только содержимое (заголовок/кнопки).
    Локаторы привязаны к атрибутам элементов (name/placeholder/class/text),
    без абсолютных путей и без порядковых индексов.
    """

    FORM = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]",
    )

    TITLE = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]//h1",
    )

    NEED_AUTH_TO_CREATE_AD_TITLE = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]"
        "//h1"
        "[contains(translate(normalize-space(.), 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',"
        " 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'), 'разместить')"
        " and contains(translate(normalize-space(.), 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',"
        " 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'), 'авториз')]")

    LOGIN_EMAIL = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]"
        "//input[@name='email' and @placeholder='Введите Email']",
    )
    LOGIN_PASSWORD = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]"
        "//input[@name='password' and @type='password' and @placeholder='Пароль']",
    )
    LOGIN_SUBMIT = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]"
        "//button[@type='submit' and normalize-space()='Войти']",
    )
    NO_ACCOUNT = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]"
        "//button[@type='button' and normalize-space()='Нет аккаунта']",
    )

    REG_TITLE = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]"
        "//h1[normalize-space()='Зарегистрироваться']",
    )
    REG_EMAIL = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]"
        "//input[@name='email' and @placeholder='Введите Email']",
    )
    REG_PASSWORD = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]"
        "//input[@name='password' and @type='password' and @placeholder='Пароль']",
    )
    REG_REPEAT_PASSWORD = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]"
        "//input[@name='submitPassword' and @type='password' and @placeholder='Повторите пароль']",
    )
    CREATE_ACCOUNT = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]"
        "//button[@type='submit' and normalize-space()='Создать аккаунт']",
    )
    HAVE_ACCOUNT = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]"
        "//button[@type='button' and normalize-space()='Уже есть аккаунт']",
    )

    ERROR_TEXT = (
        By.XPATH,
        "//form[.//input[@name='email' and @placeholder='Введите Email']]"
        "//span[contains(@class,'input_span')]",
    )

