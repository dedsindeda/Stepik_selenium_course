import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = r"https://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys(str(element.id))

    button_send = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_send.click()


    # button_send = driver.find_element(By.CSS_SELECTOR, "button.btn")
    # button_send.click()


finally:
    time.sleep(30)  # 21.24015393353145 ## //button[@type="submit"]
    browser.quit()
