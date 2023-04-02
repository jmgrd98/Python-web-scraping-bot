from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

with open('restaurant_scraping.csv', 'w') as file:
    file.write("Restaurant Title;  Menu Title;  Items \n")


service = Service(ChromeDriverManager().install())

urls = [
    'https://www.corebyclaresmyth.com/home/menus/',
    'https://hakkasan.com/mayfair/menu/',
    'https://rivercafe.com/dinner-menu/'
    ]

item_counter = 0
items_1 = []
items_2 = []

ctrl_c = Keys.CONTROL + 'C'
ctrl_v = Keys.CONTROL + 'V'

browser = webdriver.Chrome()

for url in urls:
    browser.get(url)
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')
    print(soup.prettify())
    time.sleep(1)

    if url == urls[0]:
        restaurant_title = 'CORE by Clare Smith'
        menu_title = browser.find_element(By.XPATH, '//*[@id="primary"]/div/div[1]/div/div[1]/div[1]/h3')
        print(restaurant_title)
        print(menu_title.text)

        with open('restaurant_scraping.csv', 'a') as file:
                file.write(restaurant_title  + '\n')
                file.write(menu_title.text  + '\n')

        while item_counter < 7:
            item_xpath = '//*[@id="primary"]/div/div[1]/div/div[1]/div[1]/p[{}]'
            item_xpath = item_xpath.format(item_counter + 1)
            
            item = browser.find_element(By.XPATH, item_xpath)
            items_1.append(item.text)
            item_counter += 1
            print(item.text)

            with open('restaurant_scraping.csv', 'a') as file:
                file.write(item.text + '\n')
        
        item_counter = 0


    if url == urls[1]:
        # html_text = requests.get('https://hakkasan.com/mayfair/menu/')
        # print(html_text)
        restaurant_title = 'Hakkasan Mayfair'
        menu_button_xpath = '//*[@id="menu-nav"]/ul/li[9]/a'
        # menu_button = browser.find_element(By.CLASS_NAME, 'current')
        # menu_button.click()
        # menu_title_xpath = '//*[@id="menu-3808555"]/div[1]'
        # menu_title = browser.find_element(By.XPATH, menu_title_xpath)
        print(restaurant_title)
        # print(menu_title.text)

        with open('restaurant_scraping.csv', 'a') as file:
                file.write(restaurant_title  + '\n')
                
            
    if url == urls[2]:
        restaurant_title = 'River Café'
        menu_title = browser.find_element(By.XPATH, '//*[@id="page-78"]/section/div[1]/div/div/div/div[2]/div/h1/strong')
        print(restaurant_title)
        print(menu_title.text)
        with open('restaurant_scraping.csv', 'a') as file:
                file.write(restaurant_title  + '\n')
                file.write(menu_title.text  + '\n')

        while item_counter <= 2:
           item_xpath2 = '//*[@id="page-78"]/section/div[2]/div/div/div/div[8]/div/div[{}]/div/div/p[1]'
           item_xpath2 = item_xpath2.format(item_counter + 1)

           item_2 = browser.find_element(By.XPATH, item_xpath2) 
           items_2.append(item_2)
           item_counter += 1
           print(item_2.text)
           with open('restaurant_scraping.csv', 'a') as file:
                file.write(item_2.text + '\n')


input("Press enter to close the browser...")