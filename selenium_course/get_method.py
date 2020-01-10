import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    num_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = driver.find_element_by_partial_link_text(num_link)
    link.click()

    first_name = driver.find_element_by_name("first_name")
    first_name.send_keys("python")

    last_name = driver.find_element_by_name("last_name")
    last_name.send_keys("selenium")

    city = driver.find_element(By.CLASS_NAME, "city")
    city.send_keys("in")

    country = driver.find_element(By.ID, "country")
    country.send_keys("ru")

    submit_button = driver.find_element(By.CLASS_NAME, "btn ")
    submit_button.click()

    time.sleep(13)

finally:
    driver.quit()
