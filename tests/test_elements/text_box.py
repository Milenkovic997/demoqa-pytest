from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Elements_TextBox:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def test_elements_textbox(self):
        # Elements -> Text Box
        self.driver.get("https://demoqa.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) svg").click()
        self.driver.find_element(By.CSS_SELECTOR, ".show #item-0 > .text").click()

        self.driver.find_element(By.ID, "userName").click()
        self.driver.find_element(By.ID, "userName").send_keys("Stefan Milenkovic")
        self.driver.find_element(By.ID, "userEmail").click()
        self.driver.find_element(By.ID, "userEmail").send_keys("stefan@gmail.com")
        self.driver.find_element(By.ID, "currentAddress").click()
        self.driver.find_element(By.ID, "currentAddress").send_keys("test123")
        self.driver.find_element(By.ID, "permanentAddress").click()
        self.driver.find_element(By.ID, "permanentAddress").send_keys("test123")
        self.driver.find_element(By.ID, "submit").click()

        assert self.driver.find_element(By.ID, "name").text == "Name:Stefan Milenkovic"
        assert self.driver.find_element(By.ID, "email").text == "Email:stefan@gmail.com"
        assert self.driver.find_element(By.XPATH, "//p[@id=\"currentAddress\"]").text == "Current Address :test123"
        assert self.driver.find_element(By.XPATH, "//p[@id=\"permanentAddress\"]").text == "Permananet Address :test123"