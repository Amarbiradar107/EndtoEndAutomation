import pytest

from pages.Rigistration_page import RegistrationPage


@pytest.mark.usefixtures("setup")
class TestRegistration:
    @pytest.mark.skip(reason="This test is skipped because it's just a placeholder for registration tests.")
    def test_registration(self, setup):
        registration_page = RegistrationPage(setup)
        registration_page.click_signup_link()

    @pytest.mark.skip(reason="This test is skipped because it's just a placeholder for registration tests.")
    def test_positive_registration(self, setup):
        registration_page = RegistrationPage(setup)
        registration_page.click_signup_link()
        registration_page.positive_registration("John", "Doe", "jhon@gmail.com", "password123")

    def test_negative_registration(self, setup):
        registration_page = RegistrationPage(setup)
        registration_page.click_signup_link()
        registration_page.negative_registration()


