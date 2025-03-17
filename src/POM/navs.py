from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Navs:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.prismHR = (By.XPATH, '//*[@id="page-wrapper"]/aside/nav/div[1]/ul/li[4]/a/div/i')
      

    def checkforprismHrredirect(self):
        """Clicks the PrismHR link, checks if a new tab opens, and handles navigation accordingly."""
        original_window = self.driver.current_window_handle
        all_windows_before = set(self.driver.window_handles)
        prism_field = self.wait.until(EC.element_to_be_clickable(self.prismHR))
        open_in_new_tab = prism_field.get_attribute("target") == "_blank"
        prism_field.click()
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > len(all_windows_before) or d.current_url != d.execute_script("return document.referrer;")
        )
        all_windows_after = set(self.driver.window_handles)
        time.sleep(10)
        if len(all_windows_after) > len(all_windows_before):
            new_window = (all_windows_after - all_windows_before).pop()
            self.driver.switch_to.window(new_window)
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            print(f"✅ Navigated to a new tab: {self.driver.current_url}")
            print(f"Title: {self.driver.title}")
            self.driver.close()
            self.driver.switch_to.window(original_window)
        else:
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            print(f"🔄 Redirected in the same tab: {self.driver.current_url}")
            print(f"Title: {self.driver.title}")
        assert "Sequoia" in self.driver.title, "Navigation failed!"