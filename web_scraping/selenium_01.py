from selenium import webdriver
import time

# 保持浏览器打开
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get("https://www.bilibili.com/video/BV1Yh411o7Sz/?p=50&spm_id_from=pageDriver&vd_source=374dfa7b72b21fad2d78dfde8af74c9c")

page_text = browser.page_source
print(page_text)

browser.quit()