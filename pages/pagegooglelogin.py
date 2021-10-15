from selenium.webdriver.common.by import By


class PageGoogleLogin:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, 'identifierId')
        self.email_next_button = (By.ID, 'identifierNext')
        self.password_input = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        self.password_next_button = (By.ID, 'passwordNext')

    def google_login(self, username, password):
        self.driver.find_element(*self.email_input).send_keys(username)
        self.driver.find_element(*self.email_next_button).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.password_next_button).click()
