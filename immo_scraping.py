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

house_price_list = []
for house_button in house_buttons:
    house_button.click()
    house_price = house_price = driver.find_element_by_xpath(
        "//*[@id='classified-header']/div/div/div[1]/div/div[2]/p/span[2]"
    )
    house_price_list.append(house_price.text)
    print(house_price_list)
    driver.back


# house_buttons[0].click()

# house_price_list = []

# house_price = driver.find_element_by_xpath(
#     "//*[@id='classified-header']/div/div/div[1]/div/div[2]/p/span[2]"
# )

# house_price_list.append(house_price.text)

# driver.back()

# house_buttons[1].click()


# for house in house_buttons:
#     driver.execute_script("arguments[0].click();", house)

#     html_house = driver.page_source

#     soup_house = BeautifulSoup(html_house, "html.parser")
#     # print(soup_house)

#     print(soup_house.prettify())

#     for i in soup_house.find_all("span", aria_hidden_="true"):
#         print(i.text)

# for i in range(10):
#      print("===================================")


#     house_price = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located(
#             (
#                 By.XPATH,
#                 "//*[starts_with(@id, 'lazy-loading-observer-wrapper-f9a527fa-88bb-495e-9a76-e3ea9943cb3c-classified_')]",
#             )
#         )
#     )

#     house_price_list.append(house_price.text)

# print(house_price_list)

#     house_price = driver.find_element_by_xpath(
#         "//*[@id='classified-header']/div/div/div[1]/div/div[2]/p/span[2]"
#     )

# print(house_price.text)

# house_button = WebDriverWait(driver, 13).until(
#     EC.presence_of_element_located((By.ID, (id_no[i])))

# house_button.click()
