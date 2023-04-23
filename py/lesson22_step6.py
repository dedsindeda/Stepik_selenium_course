import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = r"https://suninjuly.github.io/execute_script.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    x_value = driver.find_element(By.ID, "input_value")
    result = calc(x_value.text)

    driver.execute_script("window.scrollBy(0,100)")

    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(result)

    robot_checkbox = driver.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robot_radio_button = driver.find_element(By.ID, "robotsRule")
    robot_radio_button.click()

    button_send = driver.find_element(By.TAG_NAME, "button")
    button_send.click()

finally:
    time.sleep(10)  # 28.93909772932557
    driver.quit()
