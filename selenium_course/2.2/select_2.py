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
    browser.execute_script("document.title='Script executing';alert('Robots at work');")


finally:
    time.sleep(5)
    browser.quit()
