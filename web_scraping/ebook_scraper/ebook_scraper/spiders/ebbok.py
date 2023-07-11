import scrapy
from ebook_scraper.items import EbookScraperItem
from scrapy.loader import ItemLoader


class EbookSpider(scrapy.Spider):
	name = "ebook"
	start_urls = ["https://books.toscrape.com/"]

	def parse(self, response):

		#print(response.css("h3 a::text").get())

		#css selector
		ebooks = response.css("article")
		#xpath selector
		response.xpath("//h3/a/text()")
		list = response.xpath('//ol[@class="row"]/li')
		for li in list:
			loader = ItemLoader(item=EbookScraperItem())
			loader.add_value('title', li.xpath('./article/h3/a/@title').get())
			loader.add_value('price', li.xpath('./article/div[@class="product_price"]/p/text()').get())

			#item['title'] = li.xpath('./article/h3/a/@title').get()
			#item['price'] = li.xpath('./article/div[@class="product_price"]/p/text()').get()
			#print(title)			
			#print(price)
	
			yield loader.load_item()
