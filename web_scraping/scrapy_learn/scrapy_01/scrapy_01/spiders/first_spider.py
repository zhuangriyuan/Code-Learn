import scrapy


class FirstSpiderSpider(scrapy.Spider):
    name = "first_spider"
    #allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.bilibili.com/"]

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