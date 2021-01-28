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

url_immo_web = "https://www.immoweb.be/en"
request_immo_web = requests.get(url_immo_web)
print(url_immo_web, request_immo_web.status_code)

with open("immoweb_html.html") as immo_web_html_file:
    soup = BeautifulSoup(immo_web_html_file, "lxml")


# locate sort button
sort_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "input--select__toggle-icon"))
)
# click on locate button
driver.execute_script("arguments[0].click();", sort_button)


# return the new page
