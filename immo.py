from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time
import json
from selenium.common.exceptions import NoSuchElementException

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito') ##Accessing incognito mode 
# options.add_argument('--headless')


##Launching driver & immo website
PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.immoweb.be/en")

time.sleep(2)  
try:
    if driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]'):
        cookies=driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]')
        cookies.click()
        time.sleep(1)
except NoSuchElementException:
    pass

#cookies=driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]')
#cookies.click()

time.sleep(1)  

search=driver.find_element_by_xpath('//*[@id="searchBoxSubmitButton"]/span')
search.click()

houses = driver.find_elements_by_class_name('search-results__item')
houses_links=[]
for i in houses:
    try:
        if i.find_element_by_tag_name('h2'):
            hh1=i.find_element_by_tag_name('h2')
            hhh1=hh1.find_element_by_tag_name('a')
            house1 = hhh1.get_property('href')
            houses_links.append(house1)
    except NoSuchElementException:
        pass

print(houses_links)
time.sleep(2) 

#driver.find_element_by_xpath('//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[2]/a').click()

next_page_links = []
next_page_links.append('//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[5]/a')
'''next_page_links.append('//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[7]/a')
next_page_links.append('//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[8]/a')
for j in range(1):
    next_page_links.append('//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[9]/a')'''

for k in next_page_links:
    driver.find_element_by_xpath(k).click()
    houses = driver.find_elements_by_class_name('search-results__item')
    for i in houses:
        try:
            if i.find_element_by_tag_name('h2'):
                hh1=i.find_element_by_tag_name('h2')
                hhh1=hh1.find_element_by_tag_name('a')
                house1 = hhh1.get_property('href')
                houses_links.append(house1)
        except NoSuchElementException:
            pass
    print(houses_links)
    print('=================================================')
    print('=================================================')
    print('=================================================')
    print('=================================================')
    print('=================================================')
    time.sleep(2) 
driver.close()
#check each houses information 
number = 1
for i in houses_links:
    PATH = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get(i)
    try:
        if driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]'):
            cookies=driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]')
            cookies.click()
            time.sleep(1)
    except NoSuchElementException:
        pass
    '''time.sleep(5)  
    cookies=driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]')
    cookies.click()'''
    try:
        if driver.find_element_by_xpath('//*[@id="classified-header"]/div/div/div[1]/div/div[2]/p/span[2]'):
            price = driver.find_element_by_xpath('//*[@id="classified-header"]/div/div/div[1]/div/div[2]/p/span[2]')
            print(f'house {number}')
            number += 1
            print(f'price {price.text}')
    except NoSuchElementException:
        pass
    
    try:
        if driver.find_element_by_xpath('//*[@id="accordion_7a0d4f92-4204-4541-836a-7e82808218e1"]/table/tbody/tr[3]/td/text()'):
            price = driver.find_element_by_xpath('//*[@id="accordion_7a0d4f92-4204-4541-836a-7e82808218e1"]/table/tbody/tr[3]/td/text()')
            print(price)
    except NoSuchElementException:
        pass
    
    
    
    
    driver.close()
   # price = 
    #print(price.text)
    
    
    
    
'''#next button xpath
//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[5]/a
//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[7]/a
//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[8]/a
//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[9]/a
//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[9]/a
//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[9]/a

#p2 xpath
//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[2]/a
//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[3]/a

#p1 xpath
//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[1]/a
//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[2]/a

#driver.find_element_by_xpath('//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[2]/a').click()

#house=driver.find_element_by_xpath('//*[@id="card-a5ece71f-5486-45bf-b58b-0f7accddd28a-title"]/a')
#house.click()'''

'''houses = driver.find_elements_by_class_name('search-results__item')
del houses[1]
number=1
for i in houses:
    hh1=i.find_element_by_tag_name('h2')
    hhh1=hh1.find_element_by_tag_name('a')
    house1 = hhh1.get_property('href')
    print(number)
    number+=1
    print(f'house {house1}')

time.sleep(4)  
driver.find_element_by_xpath('//*[@id="searchResults"]/div[4]/div/div/nav/ul/li[2]/a').click()'''

