from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Radio_Button:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def test_radio_button(self):
        # Elements -> Radio Button
        self.driver.get("https://demoqa.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) svg").click()
        self.driver.find_element(By.ID, "item-2").click()

        # Selected -> Yes
        self.driver.find_element(By.CSS_SELECTOR, ".custom-control:nth-child(2) > .custom-control-label").click()
        assert self.driver.find_element(By.CLASS_NAME, "text-success").text == "Yes"

        # Selected -> Disabled Field
        self.driver.find_element(By.CSS_SELECTOR, ".disabled:nth-child(2)").click()
        assert self.driver.find_element(By.CLASS_NAME, "text-success").text == "Yes"

        # Selected -> Impressive
        self.driver.find_element(By.CSS_SELECTOR, ".custom-control:nth-child(3) > .custom-control-label").click()
        assert self.driver.find_element(By.CLASS_NAME, "text-success").text == "Impressive"

        # Selected -> Yes
        self.driver.find_element(By.CSS_SELECTOR, ".custom-control:nth-child(2) > .custom-control-label").click()
        assert self.driver.find_element(By.CLASS_NAME, "text-success").text == "Yes"