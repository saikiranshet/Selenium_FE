import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from POM.login import LoginPage
from POM.hrservices import HRServices
import pytest


@pytest.mark.order(2)
def test_hr_navigation(driver):
    HR = HRServices(driver)
    HR.checkforhr()
    assert "HR & Payroll Services | Sequoia" in driver.title, "Navigation failed!"
    driver.back()
    assert "Home | Sequoia" in driver.title
    
@pytest.mark.order(3)
def test_hr_OffCyclePayrequest(driver):
    HR = HRServices(driver)
    HR.checkforhr()
    assert "HR Administration | Sequoia" in driver.title
    HR.testOffcyclePayrequest()
   