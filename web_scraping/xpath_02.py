import requests
from lxml import etree

url = "https://bj.58.com/ershoufang/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer": "https://bj.58.com/house.shtml"
}

html = requests.get(url=url, headers=headers)

print(html.text)

tree = etree.HTML(html.text)
print(tree.xpath('//div//text()'))

# 网页可以右键直接copy xpath
