from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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
