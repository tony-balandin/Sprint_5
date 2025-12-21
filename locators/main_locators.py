from selenium.webdriver.common.by import By

class MainLocators:
    # кнопка в шапке для открытия попапа
    AUTH_BTN = (By.XPATH, "//button[contains(., 'Вход и регистрация')]")

    # индикатор, что пользователь залогинен
    LOGOUT_BTN = (By.XPATH, "//button[normalize-space()='Выйти']")

    # кнопка "Разместить объявление"
    PLACE_AD_BTN = (By.XPATH, "//button[contains(., 'Разместить объявление')]")

    # блок профиля в шапке
    PROFILE_BTN = (By.CSS_SELECTOR, "div[class^='profile_profile__']")