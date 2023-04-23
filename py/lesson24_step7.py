import math
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.ui import Select, WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = r"https://suninjuly.github.io/explicit_wait2.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    WebDriverWait(driver, timeout=12).until(exp_cond.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    x_value = driver.find_element(By.ID, "input_value")
    result = calc(x_value.text)

    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(result)

    button_send = driver.find_element(By.ID, "solve")
    button_send.click()

finally:
    time.sleep(10)  # 29.029957291435778
    driver.quit()
