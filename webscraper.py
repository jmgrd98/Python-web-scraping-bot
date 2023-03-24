from selenium import webdriver
url = 'https://www.foodstyles.com/'
browser = webdriver.Chrome()
browser.get(url)

print('Hello, World!', url)