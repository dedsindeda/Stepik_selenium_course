import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = r"https://suninjuly.github.io/find_xpath_form"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    first_name_field = driver.find_element(By.TAG_NAME, "input")
    first_name_field.send_keys("Ivan")
    last_name_field = driver.find_element(By.NAME, "last_name")
    last_name_field.send_keys("Petrov")
    city_field = driver.find_element(By.CLASS_NAME, "city")
    city_field.send_keys("Smolensk")
    country_field = driver.find_element(By.ID, "country")
    country_field.send_keys("Russia")

    button_send = driver.find_element(By.XPATH, "//button[@type=\"submit\"]")
    button_send.click()


finally:
    time.sleep(30)  # 25.283205360597716
    driver.quit()
