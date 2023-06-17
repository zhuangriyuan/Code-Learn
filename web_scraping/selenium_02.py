from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from lxml import etree
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
browser = webdriver.Chrome(options=options)

browser.get("https://www.google.com/search?q=test")


#search_input = browser.find_element(By.CLASS_NAME,"gLFyf")
#By.CSS_SELECTOR,"[data-difficulty=TOTAL]"
search_input = browser.find_element(By.ID, "APjFqb")
#删除input栏中已有的文字
search_input.clear()

search_input.send_keys("iphone")
search_button = browser.find_element(By.CLASS_NAME,"Tg7LZd")
search_button.click()



browser.back()
time.sleep(1)
browser.forward()
