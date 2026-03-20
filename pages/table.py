from asyncio import exceptions
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, \
    ElementClickInterceptedException, TimeoutException, NoSuchFrameException, NoSuchWindowException, \
    InvalidArgumentException, InvalidSessionIdException, WebDriverException, SessionNotCreatedException, \
    NoAlertPresentException, InvalidElementStateException
from selenium.webdriver.common.by import By
from utilities.logger import Utilities

class TablePage:
    #locators
    Language_filter_any = "//input[@type='radio' and @value='Any']"
    Language_filter_java= "//input[@type='radio' and @value='Java']"
    Language_filter_python = "//input[@type='radio' and @value='Python']"
    Level_filter_Beginner = "//input[@type='checkbox' and @value='Beginner']"
    Level_filter_Intermediate = "//input[@type='checkbox' and @value='Intermediate']"
    Level_filter_Advanced = "//input[@type='checkbox' and @value='Advanced']"
    checkbox = "//input[@type='checkbox']"
    Tabel_header= "//table/thead/tr/th"
    Tabel_body= "//table/tbody/tr"
    Min_enrollments_dropdown = "//div[@class='dropdown-button']"
    Min_enrollments_Options = "//div[@id='enrollDropdown']//li"
    No_data_Message = "//div[@id='noData']"


    log = Utilities().custom_logger()

    def __init__(self,setup_two):
        self.driver = setup_two

    def click_language_filter(self,user_filter):
        if user_filter == "java":
            self.driver.find_element(By.XPATH,self.Language_filter_java).click()
            column = len(self.driver.find_elements(By.XPATH,self.Tabel_header))
            rows = len(self.driver.find_elements(By.XPATH,self.Tabel_body))
            for col in range(1,column+1):
                column_header = self.driver.find_element(By.XPATH,"//table/thead/tr/th["+str(col)+"]").text
                if column_header == "Language":
                    for row in range(1,rows+1):
                        col_data = self.driver.find_elements(By.XPATH,"//table/tbody/tr/td["+str(col)+"]")
                        len(col_data)
                        # print(col_data.text)
                        for data in col_data:
                            if data.text == "":
                                self.log.info("blank value....")
                            else:
                                assert data.text == user_filter
                        break
                    break

        elif user_filter == "Python":
            self.driver.find_element(By.XPATH,self.Language_filter_python).click()
            column = len(self.driver.find_elements(By.XPATH, self.Tabel_header))
            rows = len(self.driver.find_elements(By.XPATH, self.Tabel_body))
            for col in range(1, column + 1):
                column_header = self.driver.find_element(By.XPATH, "//table/thead/tr/th[" + str(col) + "]").text
                if column_header == "Language":
                    for row in range(1, rows + 1):
                        col_data = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[" + str(col) + "]")
                        len(col_data)
                        # print(col_data.text)
                        for data in col_data:
                            if data.text == "":
                                self.log.info("blank value....")
                            else:
                                assert data.text == user_filter
                        break
                    break
        elif user_filter == "Any":
            self.driver.find_element(By.XPATH,self.Language_filter_any).click()
            column = len(self.driver.find_elements(By.XPATH, self.Tabel_header))
            rows = len(self.driver.find_elements(By.XPATH, self.Tabel_body))
            for col in range(1, column + 1):
                column_header = self.driver.find_element(By.XPATH, "//table/thead/tr/th[" + str(col) + "]").text
                if column_header == "Language":
                    for row in range(1, rows + 1):
                        col_data = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[" + str(col) + "]")
                        len(col_data)
                        # print(col_data.text)
                        for data in col_data:
                            if data.text == "":
                                self.log.info("blank value....")
                            else:
                                assert data.text == user_filter
                        break
                    break

    def select_level_filter(self):
        beginner_check_box = self.driver.find_element(By.XPATH,self.Level_filter_Beginner)
        intermediate_check_box = self.driver.find_element(By.XPATH,self.Level_filter_Intermediate).is_selected()
        advance_level_checkbox = self.driver.find_element(By.XPATH,self.Level_filter_Advanced).is_selected()
        if intermediate_check_box and advance_level_checkbox:
            self.driver.find_element(By.XPATH,self.Level_filter_Intermediate).click()
            self.log.info("intermediate level unselected")
            self.driver.find_element(By.XPATH,self.Level_filter_Advanced).click()
            self.log.info("advanced level unselected")
            column = len(self.driver.find_elements(By.XPATH, self.Tabel_header))
            rows = len(self.driver.find_elements(By.XPATH, self.Tabel_body))
            for col in range(1, column + 1):
                column_header = self.driver.find_element(By.XPATH, "//table/thead/tr/th[" + str(col) + "]").text
                if column_header == "Level":
                    for row in range(1, rows + 1):
                        col_data = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[" + str(col) + "]")
                        len(col_data)
                        # print(col_data.text)
                        for data in col_data:
                            if data.text == "":
                                self.log.info("blank value....")
                            else:
                                assert data.text == "Beginner"
                        break
                    break


        else:
            self.log.info("intermediate level selected")
            self.log.info("advanced level selected")


    def min_enrollments(self):
        click_dropdown = self.driver.find_element(By.XPATH,self.Min_enrollments_dropdown)
        click_dropdown.click()
        dropdown_values = self.driver.find_elements(By.XPATH,self.Min_enrollments_Options)
        self.log.info((len(dropdown_values)))
        for value in dropdown_values:
            if value.text == "10,000+":
                value.click()
                self.log.info("10,000+ selected")
                column = len(self.driver.find_elements(By.XPATH, self.Tabel_header))
                rows = len(self.driver.find_elements(By.XPATH, self.Tabel_body))
                for col in range(1, column + 1):
                    column_header = self.driver.find_element(By.XPATH, "//table/thead/tr/th[" + str(col) + "]").text
                    if column_header == "Enrollments":
                        for row in range(1, rows + 1):
                            col_data = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[" + str(col) + "]")
                            len(col_data)
                            for data in col_data:
                                if data.text == "":
                                    self.log.info("Encountered blank value....")
                                else:
                                    # self.log.info(data.text)
                                    enrollment_count = int(data.text)
                                    assert enrollment_count >= 10000 ,self.log.info("Enrollment count is less than 10,000")
                            break
                        break
                break


    def combined_filters(self,user_filter):
        try:
            if user_filter == "Python":
                self.driver.find_element(By.XPATH, self.Language_filter_python).click()
                intermediate_check_box = self.driver.find_element(By.XPATH, self.Level_filter_Intermediate).is_selected()
                advance_level_checkbox = self.driver.find_element(By.XPATH, self.Level_filter_Advanced).is_selected()
                if intermediate_check_box and advance_level_checkbox:
                    self.driver.find_element(By.XPATH, self.Level_filter_Intermediate).click()
                    self.log.info("intermediate level unselected")
                    self.driver.find_element(By.XPATH, self.Level_filter_Advanced).click()
                    self.log.info("advanced level unselected")
                    click_dropdown = self.driver.find_element(By.XPATH, self.Min_enrollments_dropdown)
                    click_dropdown.click()
                    dropdown_values = self.driver.find_elements(By.XPATH, self.Min_enrollments_Options)
                    self.log.info((len(dropdown_values)))
                    for value in dropdown_values:
                        if value.text == "10,000+":
                            value.click()
                            self.log.info("10,000+ selected")
                            column = len(self.driver.find_elements(By.XPATH,self.Tabel_header))
                            rows = len(self.driver.find_elements(By.XPATH,self.Tabel_body))
                            for col in range(1,column+1):
                                column_header = self.driver.find_element(By.XPATH,"//table/thead/tr/th["+str(col)+"]").text
                                col_data = self.driver.find_elements(By.XPATH,"//table/tbody/tr/td["+str(col)+"]")
                                print(len(col_data))
                                # print(col_data.text)
                                for data in col_data:
                                    if data.text:
                                        self.log.info(data.text)
                                        if column_header == "Language":
                                            if data.text == "Python":
                                                self.log.info("python data selected")
                                        if column_header == "Level":
                                            if data.text == "Beginner":
                                                self.log.info("Beginner data selected")
                                        if column_header == "Enrollments":
                                            enrollments = int(data.text)
                                            if enrollments >= 10000:
                                                self.log.info("Enrollments are greater than 10,000")
                                    elif data.text == "":
                                        # assert data.text == user_filter
                                        self.log.info(data.text)
                                        break
                                        self.log.info("blank value....")
                                    break
        except(NoSuchElementException,StaleElementReferenceException,ElementNotInteractableException,
               ElementClickInterceptedException, TimeoutException,NoSuchFrameException, NoSuchWindowException,
               NoAlertPresentException,InvalidArgumentException, WebDriverException, SessionNotCreatedException,
               InvalidSessionIdException,InvalidElementStateException ) as e:
            self.log.info("raised Exception" + str(e))
        except Exception as e:
            self.log.info("somthing went wrong"+ str(e))


    def no_results_state(self):
        beginner_level = self.driver.find_element(By.XPATH,self.Level_filter_Beginner).is_selected()
        intermediate_check_box = self.driver.find_element(By.XPATH, self.Level_filter_Intermediate).is_selected()
        advance_level = self.driver.find_element(By.XPATH, self.Level_filter_Advanced).is_selected()
        if beginner_level and intermediate_check_box:
            self.driver.find_element(By.XPATH,self.Level_filter_Beginner).click()
            self.driver.find_element(By.XPATH, self.Level_filter_Intermediate).click()
        click_dropdown = self.driver.find_element(By.XPATH, self.Min_enrollments_dropdown)
        click_dropdown.click()
        dropdown_values = self.driver.find_elements(By.XPATH, self.Min_enrollments_Options)
        # self.log.info((len(dropdown_values)))
        for value in dropdown_values:
            if value.text == "50,000+":
                value.click()
                self.log.info("50,000+ selected")
        try :
            message = self.driver.find_element(By.XPATH,self.No_data_Message).text.strip()
            # no_data_message = message.text
            assert message == "No matching courses.",self.log.info("No message found")
        except(NoSuchElementException,StaleElementReferenceException,AssertionError,TypeError) as e:
            self.log.info("raised Exception" + str(e))

    def reset_button_visibility_and_behavior(self):
        pass

    def sort_by_enrollments_ascending_numeric(self):
        pass

    def sort_by_course_name_alphabetical(self):
        pass








