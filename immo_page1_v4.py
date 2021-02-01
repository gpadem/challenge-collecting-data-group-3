from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time
import json

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito') ##Accessing incognito mode 
# options.add_argument('--headless')


##Launching driver & immo website
PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.immoweb.be/en")





#print(html) print html of source page(our immo page!)

##clicking home search button (front page)

home_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "searchBoxSubmitButton"))
)
driver.execute_script("arguments[0].click();", home_button)


property_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "card__title-link"))
)
driver.execute_script("arguments[0].click();", property_button)



###Finding price of one property with x-path
house_price = driver.find_element_by_xpath(
    "//*[@id='classified-header']/div/div/div[1]/div/div[2]/p/span[2]"
)
bedrooms = driver.find_element_by_xpath(
    "//*[@id='classified-header']/div/div/div[1]/div/div[3]/p"
)


print(house_price.text)
print(bedrooms.text)