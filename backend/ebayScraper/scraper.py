# https://selenium-python.readthedocs.io
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import os 

ebay_sold_items_url = 'https://www.ebay.co.uk/'
folder = 'scraped_data'

def get_driver():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

def get_sold_items(driver):
    driver.get(ebay_sold_items_url)

    #click advanced filter
    advanced_link = driver.find_element(By.LINK_TEXT, "Advanced")
    advanced_link.click()

    # explicit wait, accept all for gdpr
    try:
        time.sleep(5)
        accept_gdpr = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="gdpr-banner-accept"]')
        ))
        accept_gdpr.click()
    except:
        driver.quit()

    #click sold items filter
    time.sleep(5)
    sold_filter_id = 'LH_Sold'
    sold_link = driver.find_element(By.ID, sold_filter_id)
    sold_link.click()

    #search for product
    searh_bar_id = '_nkw'
    search_bar = driver.find_element(By.ID, searh_bar_id)
    # make sure search bar is empty
    search_bar.clear()
    product = 'ps5'
    search_bar.send_keys(product)
    #press enter
    search_bar.send_keys(Keys.RETURN)

    #get the listed items
    listed_items_class = 'sresult' 
    try:
        time.sleep(5)
        found_items = driver.find_elements(By.CLASS_NAME, listed_items_class)
    except:
        driver.quit()
        
    return found_items


def parse_sold_item(product):
    title_tag = product.find_element(By.CLASS_NAME, 'vip')
    title = title_tag.text
    url = title_tag.get_attribute('href')

    thumbnail_tag = product.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')

    try:
        condition_tag = product.find_element(By.CLASS_NAME, 'lvsubtitle')
        condition = condition_tag.text
    except:
        try:
            condition_tag = product.find_element(By.XPATH, "//div[contains(@class, 'lvsubtitle')]")
            condition = condition_tag.text
        except:
            pass
    
    price_tag = product.find_element(By.CLASS_NAME, 'bidsold')
    price = price_tag.text

    sold_time_tag = product.find_element(By.CLASS_NAME, 'tme')
    sold_time = sold_time_tag.text

    #if not, then type is buy now?
    try:
        listing_type_tag = product.find_element(By.CLASS_NAME, "lvformat")
        listing_type = listing_type_tag.text
    except:
        pass 

    #return dictionary
    return {
        'title': title,
        'url': url,
        'thumbnail_url': thumbnail_url,
        'condition': condition,
        'price': price,
        'sold_time': sold_time,
        'listing_type': listing_type
    }

def generate_data(products):
    sold_items_data = [parse_sold_item(product) for product in products[0:10]]
    
    directory = f'{os.path.dirname(os.path.abspath(__file__))}/{folder}/sold.json'

    with open(directory, "w") as file:
        json.dump(sold_items_data, file)
    print("Finished")

    


#to run for this script only
if __name__ == "__main__":
    print('Creating driver')
    driver = get_driver()

    products = get_sold_items(driver)

    print('Parsing first page items')

    print("Creating report")
    generate_data(products)

    driver.quit()
