import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import datetime
import os



def browse_web():
    driver = webdriver.Chrome()
    driver.get("https://quotes.toscrape.com/")

    click_tag = driver.find_element(By.LINK_TEXT, 'inspirational')
    click_tag.click()

browse_web()