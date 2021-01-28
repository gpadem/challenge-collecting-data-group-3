from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.nike.com/nl/nl/checkout/tunnel")
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//div/button[@id='qa-guest-checkout-mobile']")
    )
)
driver.execute_script("arguments[0].click();", element)


search_button = driver.find_elements_by_id("searchBoxSubmitButton")
search_button.click()
