import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Test_Links:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def validate_text_appeared(self, id):
        time.sleep(2)
        assert str(id) in self.driver.find_element(By.ID, "linkResponse").text
        time.sleep(2)

    def test_links(self):
        # Elements -> Links
        self.driver.get("https://demoqa.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) > div").click()
        self.driver.find_element(By.ID, "item-5").click()

        # Switch to link 1 tab
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.ID, "simpleLink").click()
        self.vars["win9394"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win9394"])
        self.driver.close()

        # Switch to link 2 tab
        self.driver.switch_to.window(self.vars["root"])
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.ID, "dynamicLink").click()
        self.vars["win3298"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win3298"])
        self.driver.close()

        # Validate links have been clicked
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.ID, "created").click()
        self.validate_text_appeared(201)

        self.driver.find_element(By.ID, "unauthorized").click()
        self.validate_text_appeared(401)

        element = self.driver.find_element(By.ID, "invalid-url")
        self.driver.execute_script("arguments[0].click();", element)
        self.validate_text_appeared(404)

