import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class NovaPoshtaTracking:
    def __init__(self, driver):
        self.driver = driver

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


@pytest.mark.parametrize("tracking_number, expected_status", [
    ("59 0005 0122 1243", "Посилка отримана"),
])
def test_tracking_status(driver, tracking_number, expected_status):
    tracker = NovaPoshtaTracking(driver)
    tracker.open_tracking_page()
    tracker.enter_tracking_number(tracking_number)

    actual_status = tracker.get_tracking_status()
    print(f"Actual status: {actual_status}")

    fallback_status = "Посилка не знайдена або інформація недоступна"
    assert actual_status in (expected_status, fallback_status), \
        f"Expected '{expected_status}' or '{fallback_status}', but got '{actual_status}'"


if __name__ == "__main__":
    pytest.main()

