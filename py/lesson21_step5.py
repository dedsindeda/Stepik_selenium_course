import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# http://suninjuly.github.io/registration2.html
link = r"https://suninjuly.github.io/math.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    x_value = driver.find_element(By.ID, "input_value")
    result = calc(x_value.text)

    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(result)

    robot_checkbox = driver.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robot_radio_button = driver.find_element(By.ID, "robotsRule")
    robot_radio_button.click()

    button_send = driver.find_element(By.TAG_NAME, "button")
    button_send.click()

finally:
    time.sleep(5)  # 28.892230353529506
    driver.quit()
