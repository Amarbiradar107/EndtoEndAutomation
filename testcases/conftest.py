from pathlib import Path

import pytest
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser

ROOT_DIR = Path(__file__).resolve().parent.parent

config = configparser.ConfigParser()
config.read(ROOT_DIR/'configfiles'/'config.ini')

base_url = config["environment"]["base_url"]
grid_url = config["environment"]["grid_url"]

@pytest.fixture(scope="function")
def setup(request):
    # if browser == "chrome":
    #     driver = webdriver.Chrome()
    # elif browser == "firefox":
    #     driver = webdriver.Firefox()
    # elif browser == "edge":
    #     driver = webdriver.Edge()
    # driver.maximize_window()
    options = Options()
    # options.add_argument("--log-level=3")
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # username, password = request.param
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Remote(
    #     command_executor="http://localhost:4444/wd/hub",
    #     options=options
    # )
    driver.maximize_window()
    driver.get(base_url)
    request.cls.driver = driver
    # login_page = LoginPage(driver)
    # login_page.login(username, password)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setup_two(request,):
    options_two = Options()
    # options_two.add_argument("--log-level=3")
    # options_two.add_argument("--headless")
    # options_two.add_argument("--no-sandbox")
    # options_two.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options_two)
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-table/")
    request.cls.driver = driver
    assert driver.current_url == "https://practicetestautomation.com/practice-test-table/"
    yield driver
    driver.quit()
