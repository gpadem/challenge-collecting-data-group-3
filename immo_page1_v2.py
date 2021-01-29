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

"""get url of page 1 
html = driver.page_source 
soup = BeautifulSoup(html, "html.parser") 
all_houses = soup

#searhing for all houses page 1
links_html = soup.find_all('a', class_='card__title-link')
for link in links_html:
    driver.get(link)  
    soup = BeautifulSoup(html, "html.parser") 
    print(soup)

##clicking property search button (front page)

property_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "card__title-link"))
)"""
house_buttons = driver.find_elements_by_xpath("//*[starts-with(@id, 'classified_')]")
for house in house_buttons:
    driver.execute_script("arguments[0].click();", house)

    html = driver.page_source 
      
    # this renders the JS code and stores all 
    # of the information in static HTML code. 
      
    # Now, we could simply apply bs4 to html variable 
    soup = BeautifulSoup(html, "html.parser") 
    print(soup)
    for i in range(10):
        print('===================================')
    
    """house_price = driver.find_element_by_xpath(
        "//*[@id='classified-header']/div/div/div[1]/div/div[2]/p/span[2]"
    )
    
    print(house_price.text)

driver.back()


# house button

house_buttons = driver.find_elements_by_xpath("//*[starts-with(@id, 'classified_')]")
for house in house_buttons:
    house.click()
    house_price = driver.find_element_by_xpath(
         "//*[@id='classified-header']/div/div/div[1]/div/div[2]/p/span[2]")
    print(house_price.text)"""
