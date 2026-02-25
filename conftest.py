import pytest
from selenium import webdriver
from UIPage import UIPage as uip


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.maximize_window()
    page = uip(browser)
    page.open_main_page()
    yield browser
    browser.quit()


@pytest.fixture(params=["chrome", "firefox", "edge"])
def cross(request):
    browser_name = request.param

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")

    driver.implicitly_wait(3)
    driver.maximize_window()

    yield driver
    driver.quit()