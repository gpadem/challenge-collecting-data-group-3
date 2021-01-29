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
search_button = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "searchBoxSubmitButton"))
)
# click on search button
search_button.click()

# search results per page
# search_results = driver.find_elements_by_xpath("//*[@id='main-content']")[0].text
# print(search_results)


# search_results_list = []
# for i in range(len(search_results)):
#     search_results_list.append(i)

# print(search_results_list)


# # # return the new page
# # current_url_immo_web = driver.current_url

# house button

house_buttons = driver.find_elements_by_xpath("//*[starts-with(@id, 'classified_')]")
print(house_buttons)
for house in house_buttons:
    house.click()

#     house_price = driver.find_element_by_xpath(
#         "//*[@id='classified-header']/div/div/div[1]/div/div[2]/p/span[2]"
#     )

# print(house_price.text)

# house_button = WebDriverWait(driver, 13).until(
#     EC.presence_of_element_located((By.ID, (id_no[i])))

# house_button.click()
