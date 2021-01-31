from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import re
import lxml.html
import time
from fake_useragent import UserAgent

# open driver
driver = webdriver.Chrome()

# go to url
driver.get("https://www.immoweb.be/en")

# locate search button
search_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "searchBoxSubmitButton"))
)
# click on search button
driver.execute_script("arguments[0].click();", search_button)

# object list of real_estate buttons
real_estate_buttons = driver.find_elements_by_xpath(
    "//*[starts-with(@id, 'classified_')]"
)

for real_estate in range(len(real_estate_buttons)):
    property_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "card__title-link"))
    )
    driver.execute_script("arguments[0].click();", property_button)
    wait = WebDriverWait(driver, 15)
    driver.back()

# house_button = (
#     WebDriverWait(driver, 20)
#     .until(
#         EC.presence_of_element_located(
#             (By.PARTIAL_LINK_TEXT, "https://www.immoweb.be/en/classified/")
#         )
#     )
#     .click
# )
# driver.back()

# ActionChains(driver).move_to_element(i).perform
# i.click()
# wait = WebDriverWait(driver, 15)
# driver.back()

# property_button = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "card__title-link"))
# )

# driver.execute_script("arguments[0].click();", property_button)


# price_list = []
# for real_estate in range(len(real_estate_buttons) - 1):
#     real_estate_buttons[real_estate].click()  # go to individual real estate page
#     WebDriverWait(driver, 10).until(EC.staleness_of(real_estate_buttons[real_estate]))
#     house_data = driver.find_element_by_class_name("main")
#     all_data_house = house_data.text
#     price_house = re.findall(r"(\d{6,7}\s\€)", all_data_house)
#     pr = re.findall(r"\d+", price_house[0])
#     price_list.append(int(pr[0]))
#     wait = WebDriverWait(driver, 10)
#     driver.back()
#     wait = WebDriverWait(driver, 20)


# print(price_list)
