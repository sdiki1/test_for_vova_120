import random, time, datetime


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def add_to_cart():
    with webdriver.Chrome() as browser:
        url = "https://web.telegram.org/a/"
        browser.get(url)
        browser.set_window_size(1920, 1080)
        time.sleep(25)
        a = "280379Vova"
        browser.find_element(By.CLASS_NAME, "form-control").send_keys(a)
        time.sleep(2)
        browser.find_element(
            By.XPATH, "/html/body/div[2]/div/div[1]/div/div/form/button"
        ).click()
        time.sleep(20)
        browser.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[12]/a",
        ).click()
        time.sleep(10)
        element = browser.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div/button",
        )
        hov = ActionChains(browser).move_to_element(element)
        hov.perform()

        # browser.find_element(By.XPATH, '')
        time.sleep(15)


add_to_cart()
