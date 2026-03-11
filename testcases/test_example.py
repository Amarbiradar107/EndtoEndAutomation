import pytest


from pages.verify_url import VerifyUrl
from testcases.conftest import setup
from utilities.logger import Utilities
import time

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_url_test(self):
        url_verify = VerifyUrl(self.driver)
        url_verify.verify_url()


