import scrapy

class BlogSpider(scrapy.Spider):
    name = 'mercadolibre'
    start_urls = ['https://www.mercadolibre.com.mx']

    def parse(self, response):
        
        for title in response.css('.ui-item__content'):
            yield {'title': title.css('.ui-item__title ::text').get()}
        for next_page in response.css('a.andes-pagination__link prefetch'):
            yield response.follow(next_page, self.parse)