class Registration_page:

    Signup_link = "//nav/a[text()='Sign up']"




    def __init__(self, driver):
        self.driver = driver



    def click_signup_link(self):
        self.driver.find_element(By.XPATH, self.Signup_link).click()