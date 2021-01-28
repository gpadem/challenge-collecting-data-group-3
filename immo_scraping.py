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

# codes to ignore handshake errors
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(chrome_options=options)


driver = webdriver.Chrome()  # open driver
driver.get("https://www.immoweb.be/en")  # go to url
# locate search button
search_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchBoxSubmitButton"))
)
# click on search button
driver.execute_script("arguments[0].click();", search_button)


url_immo_web = driver.current_url
request_immo_web = requests.get(url_immo_web)
print(url_immo_web, request_immo_web.status_code)
soup_immo_web = BeautifulSoup(request_immo_web.content, "lxml")
print(soup_immo_web)
