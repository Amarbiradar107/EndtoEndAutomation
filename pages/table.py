from selenium.webdriver.common.by import By


class TablePage:
    #locators
    Language_filter_any = "//input[@type='radio' and @value='Any']"
    Language_filter_java= "//input[@type='radio' and @value='Java']"
    Language_filter_python = "//input[@type='radio' and @value='Python']"

    Tabel_header= "//table/thead/tr/th"
    Tabel_body= "//table/tbody/tr"

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
                                print("blank value....")
                            else:
                                assert data.text == "Java"
                        break
                    break
        elif user_filter == "python":
            self.driver.driver.find_element(By.XPATH,self.Language_filter_python).click()
        else:
            self.driver.driver.find_element(By.XPATH,self.Language_filter_any).click()

