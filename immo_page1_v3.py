import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito') ##Accessing incognito mode 
# options.add_argument('--headless')


##Launching driver & immo website
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.immoweb.be/en")


##clicking home search button (front page--buy)

home_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "searchBoxSubmitButton"))
)
driver.execute_script("arguments[0].click();", home_button)



##clicking property search button (front page)

# house button
house_button = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "classified_9139582"))
)
house_button.click()

house_price = driver.find_element_by_xpath(
    "//*[@id='classified-header']/div/div/div[1]/div/div[2]/p/span[2]"
)

print(house_price.text)




