import uuid
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://qa-desk.stand.praktikum-services.ru/"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1400,900")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture(scope="session")
def valid_password() -> str:
    return "Qweasdzxc123!"


@pytest.fixture
def unique_email() -> str:
    return f"tonybalandin+{uuid.uuid4().hex[:10]}@example.com"


@pytest.fixture(scope="session")
def existing_user_credentials(base_url, valid_password):
    """
    Для теста "регистрация уже существующего пользователя"
    создаём один аккаунт один раз за сессию.
    """
    email = f"tonybalandin+existing_{uuid.uuid4().hex[:8]}@example.com"

    options = Options()
    options.add_argument("--window-size=1400,900")
    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(0)
    w = WebDriverWait(drv, 5)

    from tests.helpers import register_user
    register_user(drv, w, base_url, email, valid_password)

    drv.quit()
    return {"email": email, "password": valid_password}