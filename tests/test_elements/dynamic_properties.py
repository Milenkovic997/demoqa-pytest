import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Dynamic_property:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def test_dynamic_property(self):
        # Elements -> Dynamic Property
        self.driver.get("https://demoqa.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) path").click()
        self.driver.find_element(By.CSS_SELECTOR, "#item-8 > span").click()

        assert self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div/div[2]/div[2]/div[2]/p").is_enabled()
        assert not self.driver.find_element(By.CSS_SELECTOR, "#enableAfter").is_enabled()

        time.sleep(5)
        assert self.driver.find_element(By.CSS_SELECTOR, "#enableAfter").is_enabled()
        assert self.driver.find_element(By.CSS_SELECTOR, "#visibleAfter").is_enabled()