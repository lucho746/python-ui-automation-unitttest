from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageEstimationTool:
    def __init__(self, driver):
        self.driver = driver
        self.title = (By.XPATH, '/html/body/div[1]/div/div[1]/header/div/h6/a')

    def validate_title(self):
        title = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.title))
        return title.text
