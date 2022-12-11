import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Test_Buttons:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def test_buttons(self):
        # Elements -> Buttons
        self.driver.get("https://demoqa.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) svg").click()
        self.driver.find_element(By.ID, "item-4").click()


        # Double click first button
        element = self.driver.find_element(By.ID, "doubleClickBtn")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        assert self.driver.find_element(By.CSS_SELECTOR, "#doubleClickMessage").is_displayed()

        # Right Click
        element = self.driver.find_element(By.ID, "rightClickBtn")
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()
        assert self.driver.find_element(By.CSS_SELECTOR, "#rightClickMessage").is_displayed()

        # Id randomly generated for some reason
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#dynamicClickMessage").is_displayed()


