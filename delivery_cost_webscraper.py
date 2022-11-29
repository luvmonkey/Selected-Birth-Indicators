from selenium import webdriver
#For controlling browser
from selenium.webdriver.common.by import By
import time

# required for headless
from selenium.webdriver.safari.options import Options
import csv

# New paradigm for path
from selenium.webdriver.safari.service import Service
from selenium.common.exceptions import NoSuchElementException

#Sets my safari driver
safari_service = Service('/usr/bin/safaridriver')

#initializing driver with the above options
driver = webdriver.Safari(service=safari_service)

def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

driver.get('https://www.businessinsider.com/how-much-does-it-cost-to-have-a-baby-2018-4#alabama-1')
driver.close()

