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

    vaginal_birth_with_insurance = driver.find_element(By.XPATH, ("/html/body/section/section/section/section[3]/section/div/article/section[1]/div/section/div/div/div[" + num_for_xpath + "]/div/p[2]/text()[1]")).text
    state_dictionary['vaginal_birth_with_insurance'] = vaginal_birth_with_insurance

    vaginal_birth_without_insurance = driver.find_element(By.XPATH, ("/html/body/section/section/section/section[3]/section/div/article/section[1]/div/section/div/div/div[" + num_for_xpath + "]/div/p[2]/text()[2]")).text
    state_dictionary['vaginal_birth_without_insurance'] = vaginal_birth_without_insurance 

    cesarean_with_insurance = driver.find_element(By.XPATH, ("/html/body/section/section/section/section[3]/section/div/article/section[1]/div/section/div/div/div[" + num_for_xpath + "]/div/p[3]/text()[1]")).text
    state_dictionary['cesarean_with_insurance'] = cesarean_with_insurance

    cesarean_without_insurance = driver.find_element(By.XPATH, ("/html/body/section/section/section/section[3]/section/div/article/section[1]/div/section/div/div/div[" + num_for_xpath + "]/div/p[3]/text()[2]")).text
    state_dictionary['cesarean_without_insurance'] = cesarean_without_insurance

    return state_dictionary


# Open Window to website
driver.get('https://www.businessinsider.com/how-much-does-it-cost-to-have-a-baby-2018-4#alabama-1')
time.sleep(3)

#Create a dictionary to hold all the data
cost_dictionary_by_state = {}

for i in range (1, 51):
    cost_dictionary_by_state[i] = create_cost_dictionary_for_a_state(i)

# Close window
driver.close()

field_names = [
        'state_name', 
        'vaginal_birth_with_insurance', 
        'vaginal_birth_without_insurance', 
        'cesarean_with_insurance', 
        'cesarean_without_insurance']

# Saves data as a csv file
with open('cost_of_births_by_state_2019.csv', 'w') as birth_costs:
    wr = csv.DictWriter(birth_costs, fieldnames=field_names)
    wr.writeheader()
    for num in range(1, 51):
        wr.writerow(cost_dictionary_by_state[num])


