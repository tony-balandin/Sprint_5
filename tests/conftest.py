import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1400,900")

    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()