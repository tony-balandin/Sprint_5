from selenium.webdriver.common.by import By


class ProfilePageLocators:

    PROFILE_TITLE = (
        By.XPATH,

        "//form//h1[contains(translate(normalize-space(.), "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', "
        "'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'), 'профиль') "
        "or contains(translate(normalize-space(.), "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'profile')]"
    )


    MY_ADS_TITLE = (
        By.XPATH,
        "(//h1[contains(@class,'h1') and normalize-space()='Мои объявления'] | "
        "//div[contains(@class,'profilePage_listningBlock')][.//div[contains(@class,'profilePage_gridAndPaginaton')]]//h1)[1]",
    )


    MY_ADS_GRID_AND_PAGINATION = (
        By.CSS_SELECTOR,
        "div[class*='profilePage_gridAndPaginaton']",
    )


    MY_AD_CARD = (
        By.CSS_SELECTOR,
        "div[class*='profilePage_gridAndPaginaton'] div.card",
    )


    PAGINATION_SHELL = (
        By.CSS_SELECTOR,
        "div[class*='profilePage_gridAndPaginaton'] div[class*='pagination_shell']",
    )
    PAGINATION_STATUS = (
        By.CSS_SELECTOR,
        "div[class*='profilePage_gridAndPaginaton'] div[class*='pagination_shell'] p.spanGlobal",
    )
    PAGINATION_NEXT = (
        By.CSS_SELECTOR,
        "div[class*='profilePage_gridAndPaginaton'] div[class*='pagination_shell'] "
        "button[class*='arrowButton--right']",
    )

    @staticmethod
    def my_ad_title(title: str):

        safe_title = title.replace("'", "")
        return (
            By.XPATH,
            "//div[contains(@class,'profilePage_gridAndPaginaton')]"
            f"//div[contains(@class,'card')]//h2[contains(@class,'h2') and normalize-space(.)='{safe_title}']",
        )
