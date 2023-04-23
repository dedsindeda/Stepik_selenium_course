import math
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
# el = WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product_main>.price_color')))
# print(el.text)

#answer = math.log(int(time.time()))

# fake = Faker()
#
# print(f"{fake.email()}--")
# print(f"{fake.password()}--")

#el = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.TAG_NAME,"p"))
# //strong[contains(text(),'Coders at Work')]
# (By.XPATH, #messages > div:nth-child(1) > div > strong:contains("Coders at Work"))
# 123mail@mail.com passwordpassword


#link = "http://suninjuly.github.io/registration1.html"
#link = "http://suninjuly.github.io/registration2.html"


class TestLoginForm(unittest.TestCase):
    def test_login_form1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.CSS_SELECTOR,
                                          "body > div > form > div.first_block > div.form-group.first_class > input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR,
                                          "body > div > form > div.first_block > div.form-group.second_class > input")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR,
                                          "body > div > form > div.first_block > div.form-group.third_class > input")
            input3.send_keys("Smolensk")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            self.assertEqual(42, 42, "Should be absolute value of a number")

        finally:
            browser.quit()

    def test_login_form2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR,
                                      "body > div > form > div.first_block > div.form-group.first_class > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR,
                                      "body > div > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR,
                                      "body > div > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys("Smolensk")
        # input4 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.second_class > input")
        # input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        self.assertEqual(1, 42, "Should be absolute value of a number")
        # успеваем скопировать код за 30 секунд
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()


test_obj = TestLoginForm()
test_obj.test_login_form1()
test_obj.test_login_form2()
