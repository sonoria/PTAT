from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link_right = "http://suninjuly.github.io/registration1.html"
    link_err = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()

    # укажите link_err для страницы с ошибкой или link_right для страницы без бага
    browser.get(link_right)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector(".first_block .first")
    first_name.send_keys("python")

    last_name = browser.find_element_by_css_selector(".first_block .second")
    last_name.send_keys("selenium")

    third = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    third.send_keys("in@sads.we")

    phone = browser.find_element_by_css_selector(".second_block .first")
    phone.send_keys("84998981")

    Address = browser.find_element_by_css_selector(".second_block .second")
    Address.send_keys("selenium 5161asd516")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
