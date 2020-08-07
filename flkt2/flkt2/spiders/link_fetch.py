import scrapy
import re
from ..items import FlktLinkItem

class LinkFetchSpider(scrapy.Spider):
    name = 'link_fetch'

    start_urls = [
        'https://www.flipkart.com/search?sid=j9e%2Fm38%2Fo49&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DIFB'
    ]

    def parse(self, response):
        items = FlktLinkItem()
        links = response.css('._31qSD5').css('::attr(href)').extract()
        # clean = [re.sub(r"$ref", "", item) for item in links]
        l1 = []
        for l in links:
            if (l.startswith('/ifb')) and ('https://flipkart.com' + l not in l1):
                l1.append('https://flipkart.com' + l)
        items['links'] = l1

        yield items
