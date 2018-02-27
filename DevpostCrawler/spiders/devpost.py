import scrapy


class DevpostSpider(scrapy.Spider):
    name = 'Devpost'

    def start_requests(self):
        first_page = 1
        last_page = 355
        url = 'https://devpost.com/software/search?page=%d&query=is%%3Awinner'
        for i in range(first_page, last_page + 1):
            yield scrapy.Request(url=url % i, callback=self.parse)

    def parse(self, response):
        urls = response.css('a.link-to-software::attr(href)').extract()
        yield {
            'urls': urls
        }
