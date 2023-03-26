from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())

urls = [
    'https://www.corebyclaresmyth.com/home/menus/',
    # 'https://hakkasan.com/mayfair/menu/',
    # 'https://rivercafe.com/dinner-menu/'
    ]

itemCounter = 0

browser = webdriver.Chrome()

for url in urls:
    browser.get(url)
    title = browser.find_element('xpath', '//*[@id="primary"]/div/div[1]/div/div[1]/div[1]/h3')
    print(title.text)

    while itemCounter < 7:
        item_xpath = '//*[@id="primary"]/div/div[1]/div/div[1]/div[1]/p[{}]'
        item_xpath = item_xpath.format(itemCounter + 1)
            
        item = browser.find_element('xpath', item_xpath)
        itemCounter += 1
        print(item.text)

input("Press enter to close the browser...")