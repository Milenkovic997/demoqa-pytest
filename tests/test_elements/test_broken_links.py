import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Broken_Links:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_broken_links(self):
        self.driver.get("https://demoqa.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) svg").click()
        self.driver.find_element(By.CSS_SELECTOR, ".show #item-6 > .text").click()

        assert self.driver.find_element(By.CSS_SELECTOR, "img:nth-child(2)").is_displayed()
        assert self.driver.find_element(By.CSS_SELECTOR, "img:nth-child(6)").size.get('height') == 16

        self.driver.find_element(By.LINK_TEXT, "Click Here for Valid Link").click()
        assert self.driver.current_url == "https://demoqa.com/"

        self.driver.execute_script("window.history.go(-1)")
        self.driver.find_element(By.LINK_TEXT, "Click Here for Broken Link").click()
        assert self.driver.current_url == "http://the-internet.herokuapp.com/status_codes/500"

