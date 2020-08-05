import scrapy
import re
from ..items import AmznLinkItem

class WashIfbSpider(scrapy.Spider):
    name = 'wash_ifb_links'
    #allowed_domains = ['amazon.in']

    start_urls = [
        'https://www.amazon.in/s?i=kitchen&bbn=1380369031&rh=n%3A976442031%2Cn%3A976443031%2Cn%3A1380263031%2Cn%3A1380369031%2Cp_89%3AIFB&dc&fst=as%3Aoff&qid=1596560778&rnid=3837712031&ref=sr_pg_1',
        'https://www.amazon.in/s?i=kitchen&bbn=1380369031&rh=n%3A976442031%2Cn%3A976443031%2Cn%3A1380263031%2Cn%3A1380369031%2Cp_89%3AIFB&dc&page=2&fst=as%3Aoff&qid=1596599663&rnid=3837712031&ref=sr_pg_2'
    ]

    def parse(self, response):
        items = AmznLinkItem()
        links = response.css('.a-link-normal.a-text-normal').css('::attr(href)').extract()
        #clean = [re.sub(r"$ref", "", item) for item in links]
        l1 = []
        for l in links:
            if (l.startswith('/IFB')) and ('https://amazon.in'+l not in l1):
                l1.append('https://amazon.in'+l)
        items['links'] = l1


        yield items