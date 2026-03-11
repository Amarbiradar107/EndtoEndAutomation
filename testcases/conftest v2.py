import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

config = configparser.ConfigParser()
config.read('configfiles/config.ini')

base_url = config["environment"]["base_url"]
grid_url = config["environment"]["grid_url"]

@pytest.fixture(scope="function")
def setup(request):

    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get(base_url)
    request.cls.driver = driver
    yield driver
    driver.quit()