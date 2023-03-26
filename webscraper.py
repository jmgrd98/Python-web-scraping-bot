from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())

urls = [
    'https://www.corebyclaresmyth.com/home/menus/',
    'https://hakkasan.com/mayfair/menu/',
    'https://rivercafe.com/dinner-menu/'
    ]

itemCounter = 0
itemCounter1 = 1
itemCounter2 = 0

ctrlC = Keys.CONTROL + 'C'
ctrlV = Keys.CONTROL + 'V'

browser = webdriver.Chrome()

for url in urls:
    browser.get(url)

    if url == urls[0]:
        restaurantTitle = browser.find_element(By.XPATH, '//*[@id="primary"]/div/div[1]/div/div[1]/div[1]/h3')
        print(restaurantTitle.text)

        while itemCounter < 7:
            item_xpath = '//*[@id="primary"]/div/div[1]/div/div[1]/div[1]/p[{}]'
            item_xpath = item_xpath.format(itemCounter + 1)
            
            item = browser.find_element(By.XPATH, item_xpath)
            itemCounter += 1
            print(item.text)

    if url == urls[1]:
        try:
            restaurantTitle1 = browser.find_element(By.CLASS_NAME, 'location')
            print(restaurantTitle1.text)
        except:
            print('Could not find element with class name "location"')
            
    if url == urls[2]:

        while itemCounter2 <= 10:
           item_xpath2 = '//*[@id="page-78"]/section/div[2]/div/div/div/div[8]/div/div[{}]/div/div/p[1]'
           item_xpath2 = item_xpath2.format(itemCounter2 + 1)

           item2 = browser.find_element(By.XPATH, item_xpath2) 
           itemCounter2 += 1
           print(item2.text)


        # itemCounter = 0

input("Press enter to close the browser...")