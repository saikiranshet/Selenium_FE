import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from POM.login import LoginPage
from POM.navs import Navs
import pytest


@pytest.mark.order(1)
def test_prism_hr_navigation(driver):
    navs = Navs(driver)
    navs.checkforprismHrredirect()

   