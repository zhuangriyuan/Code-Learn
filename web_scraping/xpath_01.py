from lxml import etree

# 读取本地html
tree = etree.parse('test.html')
# <html><head><title>
r = tree.xpath('/html/head/title')

# html前的/表示从根目录开始，//表示多个层级。相当于bs4中的 >和空格
r = tree.xpath('/html/body/div')
r = tree.xpath('/html//div')


# 找到所有div，找到class-song
r = tree.xpath('//div[@class="song]')
# div class = song下面的第三个p标签
r = tree.xpath('//div[@class="song]/p[3]')

# 拿到标签中的text
r = tree.xpath('//div[@class="song]/p[3]/text()')[0]
# 拿到标签中非直系的文本内容/所有文本内容
r = tree.xpath('//div[@class="song]/p[3]//text()')[0]
# 拿到img标签中src的属性
r = tree.xpath('//div[@class="song"]/img/@src')
