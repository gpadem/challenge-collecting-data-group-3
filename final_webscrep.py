
##First try(approach)
#################################################################

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
PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.immoweb.be/en")


##clicking home search button (front page--buy)
home_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "searchBoxSubmitButton"))
)
driver.execute_script("arguments[0].click();", home_button)



##clicking property search button (front page)
property_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "card__title-link"))
)
driver.execute_script("arguments[0].click();", property_button)





# second approach
###################################################################################################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


#print(html) print html of source page(our immo page!)
PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.immoweb.be/en")


##clicking home search button (front page)
home_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "searchBoxSubmitButton"))
)
driver.execute_script("arguments[0].click();", home_button)



##Clicking on an individual house
property_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "card__title-link"))
)
driver.execute_script("arguments[0].click();", property_button)



###Finding price of one property with x-path
house_price = driver.find_element_by_xpath(
    "//*[@id='classified-header']/div/div/div[1]/div/div[2]/p/span[2]"
)

print(house_price.text)




##Third approach
################################################################################################################

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time
import json



##Launching driver & immo website
PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.immoweb.be/en")



##clicking home search button (front page)
home_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "searchBoxSubmitButton"))
)
driver.execute_script("arguments[0].click();", home_button)



##Clicking on an individual house
property_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "card__title-link"))
)
driver.execute_script("arguments[0].click();", property_button)




#prints out all data of the first house!! PERHAPS WE CAN LOOP THIS FOR OTHER HOUSES AND THEN SORT THE DATA WITH PANDAS????
house_data = driver.find_element_by_class_name("main")
print(house_data.text)
