from bs4 import BeautifulSoup
fp = open('./test.html', 'r', encoding="utf-8")
soup = BeautifulSoup(fp, 'lxml')  # lxml是bs4固定解析器
print(soup)  # 打印结果为html代码

# 或者直接爬取网上内容,不适用本地html

print(soup.a)  # 打印找到的第一个a标签
print(soup.div)

print(soup.find('div'))  # 等同于soup.div,找到第一个div并返回
# 属性定位，如果是class要加下划线，因为class在python中为关键字
print(soup.find('div', class_='song'))

soup.find_all('a')  # 返回所有符合的标签

soup.select('.tang')  # class前加. id前加#，标签不加前缀, css选择器
soup.select('.tang > ul > li > a')[0]  # 返回tang class下ul下li下中包含的第一个a标签
# 大于号表示一个层级一个层级，空格可以跳过，下面这个跳过了li标签，直接到a标签
soup.select('.tang > ul a')[0]

# 获取标签之间的文本数据，以a标签为例
soup.a.text
soup.a.string
soup.a.get_text()
# 获取标签中的属性
soup.a['href']
