from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 10


def wait_visible(driver, locator, timeout=TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def wait_clickable(driver, locator, timeout=TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def wait_invisible(driver, locator, timeout=TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(locator))


def wait_url_contains(driver, text, timeout=TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.url_contains(text))


def wait_url_is(driver, url, timeout=TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.url_to_be(url))


def wait_present(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
