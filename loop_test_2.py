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
from time import sleep
from random import randint
import numpy as np
from fake_useragent import UserAgent


pages = np.arange(3, 5, 1)

# # open driver
# driver = webdriver.Chrome()

# # go to url
# driver.get("https://www.immoweb.be/en")


for page in pages:
    page = (
        "https://www.immoweb.be/en/search/house/for-sale?countries=BE&page="
        + str(page)
        + "&orderBy=relevance"
    )
    driver = webdriver.Chrome()
    driver.get(page)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    urls = [
        item.get("href")
        for item in soup.find_all(
            "a", attrs={"href": re.compile("www.immoweb.be/en/classified")}
        )
    ]

data = []

for i in range(0, 3):
    url = urls[i]
    driver2 = webdriver.Chrome()
    driver2.get(url)
    sleep(randint(10, 20))
    soup = BeautifulSoup(driver2.page_source, "html.parser")
    my_table2 = soup.find_all(class_=["main"])

    price = soup.find_all("p", attrs={"class": "classified__price"})
    price_house = re.findall(r"(\d{6,7}\€)", str(price))
    pr = re.findall(r"\d+", str(price_house))
    for p in pr:
        data.append(int(p))


print(data)
