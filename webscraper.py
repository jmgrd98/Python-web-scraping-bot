from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

urls = [
    'https://www.corebyclaresmyth.com/home/menus/',
    'https://hakkasan.com/mayfair/menu/',
    'https://rivercafe.com/dinner-menu/'
    ]
browser = webdriver.Chrome()

for url in urls:
    browser.get(url)
    element = browser.find_element('xpath', '//*[@id="primary"]/div/div[1]/div/div[1]/div[1]/p[1]/strong')
    print(element.text)

input("Press enter to close the browser...")