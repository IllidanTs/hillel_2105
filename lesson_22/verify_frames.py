from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8000/dz.html")

    driver.switch_to.frame(driver.find_element(By.ID, "frame1"))

    input1 = driver.find_element(By.ID, "input1")
    input1.send_keys("Frame1_Secret")

    verify_button1 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    verify_button1.click()

    time.sleep(1)

    alert1 = Alert(driver)
    alert_text1 = alert1.text
    if alert_text1 == "Верифікація пройшла успішно!":
        print("Frame 1: Верифікація пройшла успішно")
    else:
        print("Frame 1: Верифікація не пройшла")

    alert1.accept()

    driver.switch_to.default_content()

    driver.switch_to.frame(driver.find_element(By.ID, "frame2"))

    input2 = driver.find_element(By.ID, "input2")
    input2.send_keys("Frame2_Secret")

    verify_button2 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    verify_button2.click()

    time.sleep(1)

    alert2 = Alert(driver)
    alert_text2 = alert2.text
    if alert_text2 == "Верифікація пройшла успішно!":
        print("Frame 2: Верифікація пройшла успішно")
    else:
        print("Frame 2: Верифікація не пройшла")

    alert2.accept()

finally:
    driver.quit()
