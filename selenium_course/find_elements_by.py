import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

#считаем количество элементов

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    elements2 = len(elements)
    print (elements2)

finally:
    time.sleep(3)
    browser.quit()

