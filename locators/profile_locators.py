from selenium.webdriver.common.by import By


class ProfileLocators:
    # Якорь страницы/блока "Мои объявления"
    MY_ADS_TITLE = (By.XPATH, "//*[normalize-space()='Мои объявления']")

    # Карточка объявления по заголовку
    AD_BY_TITLE = (
        By.XPATH,
        "//*[normalize-space()='Мои объявления']"
        "/following::*[contains(normalize-space(), '{title}')][1]"
    )