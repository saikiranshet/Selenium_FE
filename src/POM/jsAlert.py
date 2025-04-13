import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JSAlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Buttons to trigger the different alerts
        self.js_alert_button = (By.XPATH, '//*[@onclick="jsAlert()"]')
        self.js_confirm_button = (By.XPATH, '//*[@onclick="jsConfirm()"]')
        self.js_prompt_button = (By.XPATH, '//*[@onclick="jsPrompt()"]')

        # Result message after handling the alert
        self.result_message = (By.ID, 'result')

    def click_js_alert(self):
        """Click to trigger JS Alert"""
        self.wait.until(EC.element_to_be_clickable(self.js_alert_button)).click()

    def click_js_confirm(self):
        """Click to trigger JS Confirm"""
        self.wait.until(EC.element_to_be_clickable(self.js_confirm_button)).click()

    def click_js_prompt(self):
        """Click to trigger JS Prompt"""
        self.wait.until(EC.element_to_be_clickable(self.js_prompt_button)).click()

    def handle_alert(self, action='accept', text=None):
        """Handle alert (accept, dismiss or send text to prompt)"""
        alert = Alert(self.driver)
        if action == 'accept':
            alert.accept()
        elif action == 'dismiss':
            alert.dismiss()
        elif action == 'send_keys' and text:
            alert.send_keys(text)
            alert.accept()

    def get_result_message(self):
        """Return result message after interacting with the alert"""
        return self.wait.until(EC.visibility_of_element_located(self.result_message)).text
