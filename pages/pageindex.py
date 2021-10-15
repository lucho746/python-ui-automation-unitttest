from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from helpers.credentials import *
from pages.pagegooglelogin import PageGoogleLogin


class PageIndex:
    def __init__(self, driver):
        self.driver = driver
        self.login_button = (By.CLASS_NAME, 'login-button')

    def login(self):
        # Setup wait for later
        wait = WebDriverWait(self.driver, 10)
        # Store the ID of the original window
        original_window = self.driver.current_window_handle

        # Click the login button
        login_btn = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.login_button)
        )
        login_btn.click()

        # Wait for the new window or tab
        wait.until(expected_conditions.number_of_windows_to_be(2))

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        # Google Auth Page
        page_google_login = PageGoogleLogin(self.driver)
        page_google_login.google_login(username=username, password=password)

        # Switch back to the original window
        self.driver.switch_to.window(original_window)
