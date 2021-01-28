import bs4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# codes to ignore handshake errors
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(chrome_options=options)


driver = webdriver.Chrome()  # open driver
driver.get("https://www.immoweb.be/en")  # go to url
# locate search button
search_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "searchBoxSubmitButton"))
)
# click on search button
driver.execute_script("arguments[0].click();", search_button)


# locate sort button
sort_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "input--select__toggle-icon"))
)
# click on locate button
driver.execute_script("arguments[0].click();", sort_button)

# advanced search

driver = webdriver.Chrome()  # open driver
driver.get("https://www.immoweb.be/en")  # go to url
# locate search button
advanced_search_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            ('//*[@id="homepage-app"]/div[2]/div/div[1]/form/div[3]/div[3]/a/span'),
        )
    )
)
# click on search button
advanced_search_button.click()
