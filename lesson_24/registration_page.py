from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://guest:welcome2qauto@qauto2.forstudy.space/"

    def load(self):
        self.driver.get(self.url)

    def click_sign_up(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Sign up"]'))
        ).click()

    def enter_first_name(self, first_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'signupName'))
        ).send_keys(first_name)

    def enter_last_name(self, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'signupLastName'))
        ).send_keys(last_name)

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'signupEmail'))
        ).send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'signupPassword'))
        ).send_keys(password)

    def confirm_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'signupRepeatPassword'))
        ).send_keys(password)

    def click_signup_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Register"]'))
        ).click()
