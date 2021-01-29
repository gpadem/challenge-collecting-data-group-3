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

# # codes to ignore handshake errors
# options = webdriver.ChromeOptions()
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--ignore-ssl-errors")
# driver = webdriver.Chrome(chrome_options=options)

# add a header to not get kicked out
# user_agent = UserAgent()
# headers = {"User-Agent": str(user_agent.chrome)}

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

# # return the new page
# current_url_immo_web = driver.current_url

# house button
house_button = WebDriverWait(driver, 13).until(
    EC.presence_of_element_located((By.ID, "classified_9139582"))
)
house_button.click()

driver.back()

# get the html of the page
# request_immo_web = requests.get(current_url_immo_web, headers=headers)
# print(current_url_immo_web, request_immo_web.status_code)
# soup_immo_web = BeautifulSoup(request_immo_web.content, "lxml")
# print(soup_immo_web.prettify())


"""
would work if it was all html, so maybe on a different website
"""
# # get the link of each house
# link_house = soup_immo_web.find_all("a", class_="card__title-link")
# link_house_v1 = [str(x) for x in link_house]
# pattern = 'href="(.*)">'
# link_house_v2 = [re.search(pattern, x).group(1) for x in link_house_v1]
# print(link_house_v2)
