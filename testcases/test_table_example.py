import time

import pytest

from pages.table import TablePage


@pytest.mark.usefixtures("setup_two")
class TestTableExample:

    def test_language_filter(self,setup_two):
        tb = TablePage(setup_two)
        tb.click_language_filter("java")
        time.sleep(2)

    def test_level_filter(self,setup_two):
        tb = TablePage(setup_two)
        tb.select_level_filter()
        time.sleep(2)





