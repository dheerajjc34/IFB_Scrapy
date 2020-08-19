import scrapy


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'

    start_urls = []

    def parse(self, response):
        pass
