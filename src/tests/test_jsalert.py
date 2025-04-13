


import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from POM.login import LoginPage
from POM.jsAlert import JSAlertsPage    
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import yaml
import pytest


@pytest.mark.order(1)
def test_js_alert(driver):
    """Test case for handling JS Alert"""
    alerts_page = JSAlertsPage(driver)
    alerts_page.click_js_alert()
    alerts_page.handle_alert(action='accept')
    result_message = alerts_page.get_result_message()
    assert "You successfully clicked an alert" in result_message, f"Expected message not found: {result_message}"

@pytest.mark.order(2)
def test_js_confirm_accept(driver):
    """Test case for handling JS Confirm (accept)"""
    alerts_page = JSAlertsPage(driver)

    # Trigger JS Confirm
    alerts_page.click_js_confirm()

    # Handle JS Confirm (click "OK")
    alerts_page.handle_alert(action='accept')

    # Assert the result message
    result_message = alerts_page.get_result_message()
    assert "You clicked: Ok" in result_message, f"Expected message not found: {result_message}"


@pytest.mark.order(3)
def test_js_confirm_dismiss(driver):
    """Test case for handling JS Confirm (dismiss)"""
    alerts_page = JSAlertsPage(driver)

    # Trigger JS Confirm
    alerts_page.click_js_confirm()

    # Handle JS Confirm (click "Cancel")
    alerts_page.handle_alert(action='dismiss')

    # Assert the result message
    result_message = alerts_page.get_result_message()
    assert "You clicked: Cancel" in result_message, f"Expected message not found: {result_message}"


@pytest.mark.order(4)
def test_js_prompt(driver):
    """Test case for handling JS Prompt"""
    alerts_page = JSAlertsPage(driver)

    # Trigger JS Prompt
    alerts_page.click_js_prompt()

    # Handle JS Prompt (send some text and click "OK")
    alerts_page.handle_alert(action='send_keys', text="Hello Selenium!")

    # Assert the result message
    result_message = alerts_page.get_result_message()
    assert "You entered: Hello Selenium!" in result_message, f"Expected message not found: {result_message}"