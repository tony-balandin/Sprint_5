from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_TITLE = (
        By.XPATH,
        "//h1[contains(normalize-space(.), 'Мои объявления') "
        "or contains(normalize-space(.), 'My listings') "
        "or contains(normalize-space(.), 'My ads')]",
    )

    FAVORITES_TITLE = PROFILE_TITLE

    @staticmethod
    def ad_title(title: str):
        return (
            By.XPATH,
            "//div[contains(@class,'profilePage_grid') or contains(@class,'profilePage_gridAndPagination')]"
            "//div[contains(@class,'card')]"
            "//*[self::h1 or self::h2 or self::h3][normalize-space()=\"%s\"]" % title,
        )