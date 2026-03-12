import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:

    Signup_link = "//nav/a[text()='Sign up']"
    Firstname_field = "//input[@id='first_name']"
    Lastname_field = "//input[@id='last_name']"
    Email_field = "//input[@id='email']"
    # Close_Button = ".group.relative.z-50.flex.size-6.cursor-pointer.rounded-max"
    Password_field = "//input[@id='password']"
    Create_account_button = "//input[@type='submit' and @value='Create']"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)



    def click_signup_link(self):
        self.driver.find_element(By.XPATH, self.Signup_link).click()

    def positive_registration(self, first_name, last_name, email, password):
        self.driver.find_element(By.XPATH, self.Firstname_field).send_keys(first_name)
        self.driver.find_element(By.XPATH, self.Lastname_field).send_keys(last_name)
        self.driver.find_element(By.XPATH, self.Email_field).send_keys(email)
        # self.driver.find_element(By.CSS_SELECTOR, self.Close_Button).click()
        self.driver.find_element(By.XPATH, self.Password_field).send_keys(password)
        self.driver.find_element(By.XPATH, self.Create_account_button).click()


    def negative_registration(self):
        self.driver.find_element(By.XPATH, self.Create_account_button).click()
        print("Clicked on Create Account button without filling any details.")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Create_account_button).click()
        email_error_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='errors']/ul/li[1]")))
        assert "Email can't be blank." == email_error_message.text
        password_error_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='errors']/ul/li[2]")))
        assert "Password can't be blank." == password_error_message.text





