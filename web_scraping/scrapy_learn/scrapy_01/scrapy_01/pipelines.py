# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class Scrapy01Pipeline:
    file = None
    def open_spider(self,spider):
        print("start")
        self.file = open('./test.csv','w',encoding='utf-8')

    #处理item类型对象
    def process_item(self, item, spider):
        print(1)
        title = item['title']
        test = item['test']
        print(item)
        self.file.write(title + ":" + test + '\n')
        return item

        
    def close_spider(self,spider):
        print("end")
        self.file.close()


class mysqlPipeline:
    my_db = None
    cursor = None
    def open_spider(self,spider):
        self.my_db = mysql.connector.connect(
            host="10.0.0.123",
            user="remote-connect-user",
            password="970319zhuang",
            database="test",
            port=3306,
            charset="utf8"
            )

    def process_item(self,item,spider):
        self.cursor = self.my_db.cursor()
        self.cursor.execute('INSERT INTO testtable VALUES ("%s", "%s")'%(item['title'],item['test']))
        self.cursor.commit()
        return item
    
