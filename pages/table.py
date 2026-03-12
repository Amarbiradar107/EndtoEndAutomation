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
                                assert data.text == "Java"
                        break
                    break
        elif user_filter == "python":
            self.driver.driver.find_element(By.XPATH,self.Language_filter_python).click()
        else:
            self.driver.driver.find_element(By.XPATH,self.Language_filter_any).click()

    def select_level_filter(self):
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







