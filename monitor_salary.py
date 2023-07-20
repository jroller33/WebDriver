import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


import time
import datetime
import os



def check_salary():
    driver = webdriver.Chrome()
    driver.get("https://open.alabama.gov/Checkbook/Payee/Default.aspx")

    select_year = Select(driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_ddlYear'))

    select_year.select_by_value('2022')



    # year_dropdown = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_ddlYear')
    
    # year_dropdown.click()

    # select_year = Select()
    

check_salary()
#ctl00_ContentPlaceHolder1_ddlYear