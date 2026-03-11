from utilities.logger import Utilities
import time

class TestExample:
    log = Utilities().custom_logger()
    def test_url_test(self,setup):
        driver = setup
        actual_url = driver.current_url
        assert actual_url == "https://sauce-demo.myshopify.com/"
        time.sleep(5)
        self.log.info("url validation passed")

