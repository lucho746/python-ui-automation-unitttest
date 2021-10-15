import unittest
from selenium import webdriver

from pages.pageestimationtool import *
from pages.pageindex import *
from helpers.xmlReader import *


class Login(unittest.TestCase):
    def setUp(self):
        self.configuration = XMLReader()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
        self.driver.get(self.configuration.get_data('url'))
        self.page_index = PageIndex(self.driver)
        self.page_estimation_tool = PageEstimationTool(self.driver)

    def test_login(self):
        self.page_index.login()
        self.page_estimation_tool.validate_title()
        self.assertEqual(self.page_estimation_tool.validate_title(), "Estimation Tool")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
