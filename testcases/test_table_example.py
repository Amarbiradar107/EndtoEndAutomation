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

    @pytest.mark.skip(reason="This test is skipped because it's just an example and not meant to be executed.")
    def test_min_enrollments(self,setup_two):
        tb = TablePage(setup_two)
        tb.min_enrollments()
        time.sleep(2)

    def test_combine_filter(self,setup_two):
        tb = TablePage(setup_two)
        tb.combined_filters("Python")

    @pytest.mark.skip(reason="This test is skipped because it's just an example and not meant to be executed.")
    def test_no_results_state(self,setup_two):
        tb = TablePage(setup_two)
        tb.no_results_state()

    @pytest.mark.skip(reason="This test is skipped because it's just an example and not meant to be executed.")
    def test_reset_button_visibility_and_behavior(self,setup_two):
        tb = TablePage(setup_two)
        tb.reset_button_visibility_and_behavior()

    @pytest.mark.skip(reason="This test is skipped because it's just an example and not meant to be executed.")
    def test_sort_by_enrollments_ascending_numeric(self,setup_two):
        tb = TablePage(setup_two)
        tb.sort_by_enrollments_ascending_numeric()

    @pytest.mark.skip(reason="This test is skipped because it's just an example and not meant to be executed.")
    def test_sort_by_course_name_alphabetical(self,setup_two):
        tb = TablePage(setup_two)
        tb.sort_by_course_name_alphabetical()









