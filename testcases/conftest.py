import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(params=["chrome","firefox","edge"])
def driver(request):

    browser = request.param

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub",
            options=options
        )

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub",
            options=options
        )

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub",
            options=options
        )

    yield driver
    driver.quit()


def test_google(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title