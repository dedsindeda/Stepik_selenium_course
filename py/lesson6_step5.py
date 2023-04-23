import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = r"https://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()

    first_name_field = browser.find_element(By.TAG_NAME, "input")
    first_name_field.send_keys("Ivan")
    last_name_field = browser.find_element(By.NAME, "last_name")
    last_name_field.send_keys("Petrov")
    city_field = browser.find_element(By.CLASS_NAME, "city")
    city_field.send_keys("Smolensk")
    country_field = browser.find_element(By.ID, "country")
    country_field.send_keys("Russia")

    button_send = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_send.click()


    # button_send = driver.find_element(By.CSS_SELECTOR, "button.btn")
    # button_send.click()


finally:
    time.sleep(30)  # 22.33866662166898 2nd 25.229137259079877
    browser.quit()
