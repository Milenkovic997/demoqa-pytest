from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import numpy as np


class Test_Web_Tables:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def validate_number_of_rows(self, rowNumber):
        number = self.driver.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div/div[2]/div[2]/div[2]/div[3]/div["
                                                     "1]/div[2]/div[*]/div[not(contains(@class, '-padRow'))]")
        assert rowNumber == np.size(number)

    def test_web_tables(self):
        # Elements -> Web Tables
        self.driver.get("https://demoqa.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) > div").click()
        self.driver.find_element(By.ID, "item-3").click()

        # Add new
        self.driver.find_element(By.ID, "addNewRecordButton").click()
        element = self.driver.find_element(By.ID, "addNewRecordButton")

        # Enter values in fields
        self.driver.find_element(By.ID, "firstName").click()
        self.driver.find_element(By.ID, "firstName").send_keys("test")
        self.driver.find_element(By.ID, "lastName").click()
        self.driver.find_element(By.ID, "lastName").send_keys("test")
        self.driver.find_element(By.ID, "userEmail").click()
        self.driver.find_element(By.ID, "userEmail").send_keys("test@gmail.com")
        self.driver.find_element(By.ID, "age").click()
        self.driver.find_element(By.ID, "age").send_keys("1")
        self.driver.find_element(By.ID, "salary").click()
        self.driver.find_element(By.ID, "salary").send_keys("1")
        self.driver.find_element(By.ID, "department").click()
        self.driver.find_element(By.ID, "department").send_keys("test")
        self.driver.find_element(By.ID, "submit").click()
        self.validate_number_of_rows(4)

        # Edit
        self.driver.find_element(By.CSS_SELECTOR, "#edit-record-4 path").click()
        self.driver.find_element(By.ID, "age").click()
        self.driver.find_element(By.ID, "age").send_keys(Keys.BACKSPACE, "5")
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > "
                                                         "div.web-tables-wrapper > div.ReactTable.-striped.-highlight "
                                                         "> div.rt-table > div.rt-tbody > div:nth-child(4) > div > "
                                                         "div:nth-child(3)").text == '5'

        # Delete
        self.driver.find_element(By.CSS_SELECTOR, "#delete-record-3 path").click()
        self.validate_number_of_rows(3)

        # View Rows
        dropdown = self.driver.find_element(By.CSS_SELECTOR, "select")
        dropdown.find_element(By.XPATH, "//option[. = '5 rows']").click()

        # Search
        self.driver.find_element(By.ID, "searchBox").click()
        self.driver.find_element(By.ID, "searchBox").send_keys("test")
        self.validate_number_of_rows(1)

