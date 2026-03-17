import time

import pytest

from pages.table import TablePage


@pytest.mark.usefixtures("setup_two")
class TestTableExample:
    @pytest.mark.skip(reason="This test is skipped because it's just an example and not meant to be executed.")
    def test_language_filter(self,setup_two):
        tb = TablePage(setup_two)
        tb.click_language_filter("java")
        time.sleep(2)

    @pytest.mark.skip(reason="This test is skipped because it's just an example and not meant to be executed.")
    def test_level_filter(self,setup_two):
        tb = TablePage(setup_two)
        tb.select_level_filter()
        time.sleep(2)

    # @pytest.mark.skip(reason="This test is skipped because it's just an example and not meant to be executed.")
    def test_min_enrollments(self,setup_two):
        tb = TablePage(setup_two)
        tb.min_enrollments()
        time.sleep(2)

    def test_combile_filter(self,setup_two):
        tb = TablePage(setup_two)
        tb.combined_filters()






