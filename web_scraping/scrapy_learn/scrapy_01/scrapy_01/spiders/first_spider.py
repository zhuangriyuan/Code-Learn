import scrapy


class FirstSpiderSpider(scrapy.Spider):
    name = "first_spider"
    #allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.bilibili.com/"]

    def parse(self, response):
        #print("test")
        a_list = response.xpath('//div[@class="channel-items__left"]/a')
        #print(response)
        #print("#*#*#*#*#*#*#*#*#*#")
        #print(a_list)
        for a in a_list:
            title = a.xpath('./text()').extract()
            print(title)
