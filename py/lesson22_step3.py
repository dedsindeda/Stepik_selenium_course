import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = r"https://suninjuly.github.io/selects1.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    num1 = driver.find_element(By.ID, "num1").text
    num2 = driver.find_element(By.ID, "num2").text
    sum_value = int(num1)+int(num2)

    select = Select(driver.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum_value))

    button_send = driver.find_element(By.TAG_NAME, "button")
    button_send.click()

finally:
    time.sleep(10)  # 28.93773628233078
    driver.quit()
