import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()

    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_css_selector(".form-control")
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()

    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    button = browser.find_element_by_css_selector(".btn-default")
    button.click()



finally:
    time.sleep(5)
    browser.quit()
