from selenium import webdriver
from bs4 import BeautifulSoup
import pandas
import time
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

itemCounter = 0
items1 = []
items2 = []

ctrlC = Keys.CONTROL + 'C'
ctrlV = Keys.CONTROL + 'V'

browser = webdriver.Chrome()

for url in urls:
    browser.get(url)

    if url == urls[0]:
        restaurantTitle = 'CORE by Clare Smith'
        menuTitle = browser.find_element(By.XPATH, '//*[@id="primary"]/div/div[1]/div/div[1]/div[1]/h3')
        print(restaurantTitle)
        print(menuTitle.text)
        with open('restaurant_scraping.csv', 'a') as file:
                file.write(restaurantTitle  + '\n')
                file.write(menuTitle.text  + '\n')

        while itemCounter < 7:
            item_xpath = '//*[@id="primary"]/div/div[1]/div/div[1]/div[1]/p[{}]'
            item_xpath = item_xpath.format(itemCounter + 1)
            
            item = browser.find_element(By.XPATH, item_xpath)
            items1.append(item.text)
            itemCounter += 1
            print(item.text)
            with open('restaurant_scraping.csv', 'a') as file:
                file.write(item.text + '\n')
        
        itemCounter = 0


    if url == urls[1]:
        restaurantTitle = 'Hakkasan Mayfair'

        print(restaurantTitle)

        with open('restaurant_scraping.csv', 'a') as file:
                file.write(restaurantTitle  + '\n')
                
            
    if url == urls[2]:
        restaurantTitle = 'River Café'
        menuTitle = browser.find_element(By.XPATH, '//*[@id="page-78"]/section/div[1]/div/div/div/div[2]/div/h1/strong')
        print(restaurantTitle)
        print(menuTitle.text)
        with open('restaurant_scraping.csv', 'a') as file:
                file.write(restaurantTitle  + '\n')
                file.write(menuTitle.text  + '\n')

        while itemCounter <= 2:
           item_xpath2 = '//*[@id="page-78"]/section/div[2]/div/div/div/div[8]/div/div[{}]/div/div/p[1]'
           item_xpath2 = item_xpath2.format(itemCounter + 1)

           item2 = browser.find_element(By.XPATH, item_xpath2) 
           items2.append(item2)
           itemCounter += 1
           print(item2.text)
           with open('restaurant_scraping.csv', 'a') as file:
                file.write(item2.text + '\n')


input("Press enter to close the browser...")