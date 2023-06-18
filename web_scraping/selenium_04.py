from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

#无头浏览器
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
driver.get('https://www.youtube.com/')
