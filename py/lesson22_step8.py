import math
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = r"https://suninjuly.github.io/file_input.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    text_elements = driver.find_elements(By.CSS_SELECTOR, "input[type=\"text\"]")
    for element in text_elements:
        element.send_keys("Any text")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "text.txt")
    file_upload = driver.find_element(By.CSS_SELECTOR, "input[type=\"file\"]")
    file_upload.send_keys(file_path)

    button_send = driver.find_element(By.TAG_NAME, "button")
    button_send.click()

finally:
    time.sleep(10)  # 28.940006349218766
    driver.quit()
