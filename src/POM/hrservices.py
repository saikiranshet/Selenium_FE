from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class HRServices:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.hrsriceclick = (By.XPATH, '//*[@id="page-wrapper"]/aside/nav/div[3]/ul/li[2]/a/div/span')
        self.hrserviceOffCycle = (By.XPATH, '//*[@id="page-wrapper"]/section/div/div/div[3]/div/div[6]/div/h4')
        self.employeesearch = (By.CSS_SELECTOR, '#employeeName')
        self.selectEmploee = (By.XPATH, "//div[contains(text(),'Aaron Powell')]")
        self.earningpath = (By.XPATH, '//*[@id="page-wrapper"]/section/div/div/main/div/form/div[2]/div[1]/div[2]/div[1]/span')
        self.selectiionElement = (By.XPATH, "//div[contains(text(), 'Bonus')]")
        self.earningamount = (By.CSS_SELECTOR, '#amount')
        

    def checkforhr(self):
        hrservice = self.wait.until(EC.presence_of_element_located(self.hrsriceclick))
        hrservice.click()
        
    def testOffcyclePayrequest(self):
        hrOffCycle = self.wait.until(EC.presence_of_element_located(self.hrserviceOffCycle))
        hrOffCycle.click()
        hrOffCycleEmployeeSearch = self.wait.until(EC.presence_of_element_located(self.employeesearch))
        hrOffCycleEmployeeSearch.send_keys("Aaron Powell")
        time.sleep(10)
        hrselecrEmployee = self.wait.until(EC.element_to_be_clickable(self.selectEmploee))
        hrselecrEmployee.click()
        earningpath = self.wait.until(EC.element_to_be_clickable(self.earningpath))
        earningpath.click()
        # option = self.wait.until(EC.presence_of_element_located(self.selectiionElement))
        # option.click()
        # hrOffCycleEmployeearningamt = self.wait.until(EC.presence_of_element_located(self.earningamount))
        # hrOffCycleEmployeearningamt.send_keys("1000")
        # time.sleep(10)

        
    
    