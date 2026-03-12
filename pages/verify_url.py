import time

from utilities.logger import Utilities


class VerifyUrl:
    def __init__(self,driver):
        self.driver = driver

    def verify_url(self):
        log = Utilities().custom_logger()
        actual_url = self.driver.current_url
        assert actual_url == "https://sauce-demo.myshopify.com/"
        time.sleep(5)
        log.info("url validation passed")

