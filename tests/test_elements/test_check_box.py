from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Check_box:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def test_check_box(self):
        # Elements -> Check Box
        self.driver.get("https://demoqa.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) path").click()
        self.driver.find_element(By.ID, "item-1").click()

        self.driver.find_element(By.CSS_SELECTOR, ".rct-icon-uncheck").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#result").text == ('You have selected :\n'
                                                                             'home\n'
                                                                             'desktop\n'
                                                                             'notes\n'
                                                                             'commands\n'
                                                                             'documents\n'
                                                                             'workspace\n'
                                                                             'react\n'
                                                                             'angular\n'
                                                                             'veu\n'
                                                                             'office\n'
                                                                             'public\n'
                                                                             'private\n'
                                                                             'classified\n'
                                                                             'general\n'
                                                                             'downloads\n'
                                                                             'wordFile\n'
                                                                             'excelFile')

        self.driver.find_element(By.CSS_SELECTOR, ".rct-icon-expand-close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".rct-node-collapsed:nth-child(1) .rct-collapse > .rct-icon").click()
        self.driver.find_element(By.CSS_SELECTOR, ".rct-node-leaf:nth-child(1) .rct-checkbox path").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#result").text == ('You have selected :\n'
                                                                             'commands\n'
                                                                             'documents\n'
                                                                             'workspace\n'
                                                                             'react\n'
                                                                             'angular\n'
                                                                             'veu\n'
                                                                             'office\n'
                                                                             'public\n'
                                                                             'private\n'
                                                                             'classified\n'
                                                                             'general\n'
                                                                             'downloads\n'
                                                                             'wordFile\n'
                                                                             'excelFile')
