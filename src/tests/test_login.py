

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from POM.login import LoginPage
import yaml
import pytest


@pytest.mark.order(6)
def test_login(driver, config):
    login_page = LoginPage(driver)
    login_page.checkLogin(config, valid=True)
    assert "The Internet" in driver.title, "Login failed or title does not match"

@pytest.mark.order(5)
def test_invalid_login(driver, config):
    config["invalidusername"]
    config["invalidpassword"] 
    login_page = LoginPage(driver)
    login_page.checkLogin(config, False) 
    error_msg = login_page.get_error_message()
    assert "Your username is invalid!" in error_msg

