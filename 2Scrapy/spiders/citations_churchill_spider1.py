# citations_churchill_spider1.py

import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        # for cit in response.xpath('//div[@class="figsco__quote__text"]'):
        #     text_value = cit.xpath('a/text()').extract_first()
        #     text_value = text_value.lstrip(u"\u201C")
        #     text_value = text_value.rstrip(u"\u201D")
        #     #text_value = text_value.strip("“")
        #     yield { 'text' : text_value}
        # for cit in response.xpath('//div[@class="figsco__quote__from figsco__row"]'):
        #     author = cit.xpath('//*[@class="figsco__fake__col-9"]/a/text()').extract_first()
        #     yield { 'author' : author}


        for item in response.xpath('//li[@class="figsco__selection__list__evene__list__item"]'):
            text_value = item.xpath('//div[@class="figsco__quote__text"]/a/text()').extract_first()
            text_value = text_value.lstrip(u"\u201C")
            text_value = text_value.rstrip(u"\u201D")

            author = item.xpath('//div[@class="figsco__quote__from figsco__row"]//div[@class="figsco__fake__col-9"]/a/text()').extract_first()
            
            yield { 'text' : text_value, 'author' : author}
