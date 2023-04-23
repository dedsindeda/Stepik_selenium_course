import math
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = r"https://suninjuly.github.io/alert_accept.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    confirm_alert = driver.switch_to.alert
    confirm_alert.accept()

    x_value = driver.find_element(By.ID, "input_value")
    result = calc(x_value.text)

    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(result)

    button_send = driver.find_element(By.TAG_NAME, "button")
    button_send.click()

finally:
    time.sleep(10)  # 28.98327383450118
    driver.quit()
