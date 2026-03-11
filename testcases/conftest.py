import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser

config = configparser.ConfigParser()
config.read('configfiles/config.ini')

base_url = config["environment"]["base_url"]
grid_url = config["environment"]["grid_url"]

@pytest.fixture(scope="function")
def setup():
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
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options
    )
    driver.maximize_window()
    driver.get(base_url)
    # login_page = LoginPage(driver)
    # login_page.login(username, password)

    yield driver
    driver.quit()