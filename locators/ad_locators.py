from selenium.webdriver.common.by import By


class AdLocators:
    CREATE_LISTING_TITLE = (By.XPATH, "//h1[contains(normalize-space(.), 'Новое объявление')]")

    TITLE_INPUT = (By.XPATH, "//input[@name='name' and (@placeholder='Название' or @placeholder='Источник')]")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@name='description']")

    PRICE_OR_SOURCE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Стоимость' or @placeholder='Источник' or @name='price' or @name='source']"
    )

    DROPDOWN_ARROW_BY_NAME = (By.XPATH, "//input[@name='{name}']/following-sibling::button")

    DROPDOWN_OPTION_BY_TEXT = (
        By.XPATH,
        "//div[contains(@class,'dropDownMenu_options')]//button[.//font[normalize-space()='{text}'] "
        "or normalize-space(.)='{text}']"
    )

    CONDITION_USED = (By.XPATH, "//label[.//font[normalize-space()='Б/У'] or normalize-space(.)='Б/У']")
    CONDITION_NEW = (By.XPATH, "//label[.//font[normalize-space()='Новый'] or normalize-space(.)='Новый']")

    PHOTO_INPUT_1 = (By.XPATH, "//input[@type='file' and @name='img1']")
    PHOTO_INPUT_2 = (By.XPATH, "//input[@type='file' and @name='img2']")
    PHOTO_INPUT_3 = (By.XPATH, "//input[@type='file' and @name='img3']")

    PUBLISH_BTN = (By.XPATH, "//button[@type='submit' and contains(normalize-space(.), 'Опубликовать')]")

    MY_AD_ITEM_BY_TITLE = (By.XPATH, "//*[contains(@class,'listing') or contains(@class,'Listing')]//*[contains(., '{title}')]")