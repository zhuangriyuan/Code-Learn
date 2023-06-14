# coding=utf-8

import requests
from bs4 import BeautifulSoup


url = "https://www.shicimingju.com/book/sanguoyanyi.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
html = requests.get(url=url, headers=headers)
html.encoding = "utf-8"
# print(html.text)
soup = BeautifulSoup(html.text, "lxml")
mulu = soup.select(".book-mulu > ul a")
for title in mulu:
    print(title.text)
