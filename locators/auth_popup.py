from selenium.webdriver.common.by import By


class AuthPopupLocators:
    """Локаторы попапа авторизации/регистрации."""

    # Логин
    LOGIN_EMAIL = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[1]/div/div/input",
    )
    LOGIN_PASSWORD = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[2]/div/div/input",
    )
    LOGIN_SUBMIT = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[5]/form/div[3]/button[1]",
    )

    # Переход к регистрации
    NO_ACCOUNT = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[5]/form/div[3]/button[2]",
    )

    # Заголовок формы (и для регистрации, и для сценария "нужна авторизация")
    REG_TITLE = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[5]/form/div[1]/h1",
    )

    # Сценарий: пользователь не залогинен, нажал "Разместить объявление".
    NEED_AUTH_TO_CREATE_AD_TITLE = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[5]/form/div[1]/h1",
    )

    # Регистрация
    REG_EMAIL = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[1]/div/div/input",
    )
    REG_PASSWORD = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[2]/div/div/input",
    )
    REG_REPEAT_PASSWORD = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[3]/div/div/input",
    )
    CREATE_ACCOUNT = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[5]/form/div[3]/button[1]",
    )

    # Ошибка для email
    EMAIL_ERROR = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[1]/span",
    )

    # В тестах ошибку читаем одинаково
    ERROR_TEXT = EMAIL_ERROR
