import scrapy
from scrapy_01.items import Scrapy01Item

class FirstSpiderSpider(scrapy.Spider):
    name = "first_spider"
    #allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.bilibili.com/"]

    #保存csv在本地，使用terminal
    '''
        def parse(self, response):
            datas = []
            a_list = response.xpath('//div[@class="channel-items__left"]/a')
            for a in a_list:
                title = a.xpath('./text()').extract()
                dic = {
                    'title':title,
                    'test':'test'
                }
                datas.append(dic)
            print(datas)
            return datas

            #save data with terminal
            #scrapy crawl first_spider -o ./title.csv
    '''
    def parse(self, response):
        
        datas = []
        a_list = response.xpath('//div[@class="channel-items__left"]/a')
        for a in a_list:
            title = a.xpath('./text()').extract()
            title = ''.join(title)
            test = "test"

            item = Scrapy01Item()
            item['title'] = title
            item['test'] = test
            yield item
            #1.数据解析
            #2.将数据封装到item
            #3.将item提交给pipeline