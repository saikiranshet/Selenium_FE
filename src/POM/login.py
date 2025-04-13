from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.email = (By.CSS_SELECTOR, '#username')
        self.password = (By.CSS_SELECTOR, '#password')
        self.login = (By.XPATH, '//*[@id="login"]/button/i')

    def checkLogin(self, config, valid=True):
        """Login using provided credentials and validate the result."""
        self.driver.get(config["base_url"])
        username = config["username"] if valid else config["invalidusername"]
        password = config["password"] if valid else config["invalidpassword"]
        email_field = self.wait.until(EC.presence_of_element_located(self.email))
        email_field.send_keys(username)
        password_field = self.wait.until(EC.visibility_of_element_located(self.password))
        password_field.send_keys(password)
        next_button = self.wait.until(EC.element_to_be_clickable(self.login))
        next_button.click()
        if not valid:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.error")))

    def get_error_message(self):
        """Get error message in case of failed login"""
        return self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.error"))
        ).text
