# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CountryscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        field_names = ['population', 'area']
        for field_name in field_names:
            value = adapter.get(field_name)
            adapter[field_name] = float(value)
        
        return item



import mysql.connector

class SaveToMySQLPipeline:
    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin_001",
            database="countries",
            charset="utf8mb4",
            collation="utf8mb4_general_ci"
        )

        
        self.cur = self.conn.cursor()
        
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            country VARCHAR(255) NOT NULL,
            capital TEXT NOT NULL,
            population BIGINT,
            area FLOAT
        )
        """)
    
    def process_item(self, item, spider):

        self.cur.execute(""" insert into countries (
            country, 
            capital, 
            population, 
            area
            ) values (
                %s,
                %s,
                %s,
                %s
                )""", (
            item["country"],
            item["capital"],
            item["population"],
            item["area"]
        ))
        
        self.conn.commit()
        return item

    
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()