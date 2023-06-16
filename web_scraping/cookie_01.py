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
    "test": "test",
    "test": "test",
    "test": "test"
}
login_page = requests.post(url=login_url, headers=headers, data=data).text

# 对已经登录的页面爬取数据，发现还需要登录，因为服务器不知道是在已经登陆的状态下发出的请求
# 需要携带cookie
# cookie:用来让服务器记录客户端的相关状态
# 将cookie封装到headers中，cookie在登陆后的网页中在request headers中查找

# 手动cookie,不建议，因为cookie有时长限制且需要手动抓取
headers = {
    "Cookie": "xxxx"
}

# 自动处理：session
# 可以进行请求的发送，如果请求过程中产生cookie，则该cookie会被自动春促在session对象中
# 使用session对象进行模拟登录post请求的发送（cookie就会存储在session中）
session = requests.Session()
login_page = session.post(url=login_url, headers=headers, data=data).text
# 需要登录的都使用session对象，session.post/session.get
