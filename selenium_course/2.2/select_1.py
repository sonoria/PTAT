import time
import math


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link1 = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link1)
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    x = int(num1) + int(num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(x))

    button = browser.find_element_by_css_selector(".btn-default")
    button.click()


finally:
    time.sleep(5)
    browser.quit()
