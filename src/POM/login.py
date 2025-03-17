from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.email = (By.CSS_SELECTOR, '#email')
        self.verify_email = (By.XPATH, '//button[@data-testid="continue-verify-email"]')
        self.password = (By.CSS_SELECTOR, '#password')
        self.next = (By.CSS_SELECTOR, '#next')

    def checkLogin(self, config):
        self.driver.get(config["base_url"])
        email_field = self.wait.until(EC.presence_of_element_located(self.email))
        email_field.send_keys(config["username"])
        verify_button = self.wait.until(EC.element_to_be_clickable(self.verify_email))
        verify_button.click()
        password_field = self.wait.until(EC.visibility_of_element_located(self.password))
        password_field.send_keys(config["password"])
        next_button = self.wait.until(EC.element_to_be_clickable(self.next))
        next_button.click()
        self.wait.until(EC.title_contains("Sequoia Login"))
