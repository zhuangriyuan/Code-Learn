# test code for regular expression

import re
import requests

url = "https.sometesturl.com"
headers = {
    "test": "test"
}

html = requests.get(url=url, headers=headers).text
regex = '<div class="thub">.*?<img src="(.*?) alt.*?=</div>'
# 基本使用.*?进行懒惰匹配，括号中是需要拿到的数据(.*?)
regex.findall(regex, html, re.S)  # re.S单行匹配，re.M多行匹配，数据解析一般为re.S
