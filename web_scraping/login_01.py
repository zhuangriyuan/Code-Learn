import requests
from lxml import etree

headers = {
    #
}

url = "test.com"
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
# 获取验证码src
code_img_src = tree.xpath('test')[0]
# 获取图片
code_img_data = requests.get(url=code_img_src, headers=headers).content
# 保存到本地
with open('./code.jpg', 'wb') as fp:
    fp.write(code_img_data)

# 使用ddddocr识别本地验证码，代码省略

# 抓取登录后的url post请求，用谷歌开发者
login_url = "login.com"
data = {
    "test": "test"
    "test": "test"
    "test": "test"
}
login_page = requests.post(url=login_url, headers=headers, data=data).text
