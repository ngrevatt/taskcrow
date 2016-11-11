from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
from selenium.common.exceptions import NoSuchElementException



class SearchTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Remote(command_executor='http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_searchbar(self):
        self.browser.get("http://web/")
        # print(self.browser.page_source)

        elem = self.browser.find_element_by_name("query")
        elem.send_keys("rake")
        elem.submit()
        try:
            taskLink = self.browser.find_element_by_link_text("Rake leaves for $100")
        except:
            self.fail("No Rake Link Found")

