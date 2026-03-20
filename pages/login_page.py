
class LoginPage:

    User_name_field = "//input[@id='username']"
    Password_field = "//input[@id='password']"
    Submit_button = "//button[@id='submit']"
    Page_Url = "https://practicetestautomation.com/logged-in-successfully/"
    Login_message = "//div/p[contains(.,'Congratulations student. You successfully logged in!')]"
    Log_out_button = "//div/a[contains(.,'Log out')]"

    def __init__(self,setup_two):
        self.driver = setup_two


