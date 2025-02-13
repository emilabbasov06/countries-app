import scrapy
from ..items import CountryItem


class CountryspiderSpider(scrapy.Spider):
    name = "countryspider"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response):
        countries = response.css('.country')

        for country in countries:
            country_item = CountryItem()
            
            country_item['country'] = country.css('h3.country-name').get().replace('\n', '').split('</')[1].replace('i>', '').strip()
            country_item['capital'] = country.css('span.country-capital::text').get()
            country_item['population'] = country.css('span.country-population::text').get()
            country_item['area'] = country.css('span.country-area::text').get()
            
            yield country_item