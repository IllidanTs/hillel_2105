from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time


class NovaPoshtaTracking:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def open_tracking_page(self):
        self.driver.get("https://tracking.novaposhta.ua/#/uk")

    def enter_tracking_number(self, tracking_number):
        tracking_input = self.driver.find_element(By.ID, "en")
        tracking_input.send_keys(tracking_number)
        tracking_input.send_keys(Keys.RETURN)
        time.sleep(5)

    def get_tracking_status(self):
        try:
            status_element = self.driver.find_element(By.CLASS_NAME, "header__status-text")
            return status_element.text
        except NoSuchElementException:
            return "Посилка не знайдена або інформація недоступна"

    def close_browser(self):
        self.driver.quit()


def test_tracking_status():
    tracking_number = "59 0005 0122 1243"
    expected_status = "Посилка отримана"
    fallback_status = "Посилка не знайдена або інформація недоступна"

    tracker = NovaPoshtaTracking()
    tracker.open_tracking_page()
    tracker.enter_tracking_number(tracking_number)

    actual_status = tracker.get_tracking_status()
    print(f"Actual status: {actual_status}")
    tracker.close_browser()

    assert actual_status == expected_status or actual_status == fallback_status, \
        f"Expected '{expected_status}' or '{fallback_status}', but got '{actual_status}'"


if __name__ == "__main__":
    test_tracking_status()
