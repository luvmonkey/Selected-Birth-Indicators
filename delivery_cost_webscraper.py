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

def create_cost_dictionary_for_a_state(counter):
    # Create a dictionary of the cost of one state
    state_dictionary = {}

    # There is a pattern to the XPATH that follows even numbers for each of the 50 states
    num_for_xpath = str(counter * 2)

    state_name = driver.find_element(By.XPATH, ("/html/body/section/section/section/section[3]/section/div/article/section[1]/div/section/div/div/div[" + num_for_xpath + "]/div/div[1]/h2")).text
    state_dictionary['state_name'] = state_name
    print(state_name)



# Open Window to website
driver.get('https://www.businessinsider.com/how-much-does-it-cost-to-have-a-baby-2018-4#alabama-1')
time.sleep(3)

create_cost_dictionary_for_a_state(1)
create_cost_dictionary_for_a_state(2)
create_cost_dictionary_for_a_state(3)

# Close window
driver.close()

