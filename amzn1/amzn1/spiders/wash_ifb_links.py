import scrapy
import re
from ..items import AmznLinkItem

class WashIfbSpider(scrapy.Spider):
    name = 'wash_ifb_links'
    #allowed_domains = ['amazon.in']

    start_urls = [
        "https://www.amazon.in/s?bbn=1380072031&rh=n%3A976442031%2Cn%3A%21976443031%2Cn%3A1380263031%2Cn%3A1380072031%2Cp_89%3ABosch&dc&fst=as%3Aoff&qid=1596783564&rnid=3837712031&ref=sr_in_b_p_89_2"
    ]

    def parse(self, response):
        items = AmznLinkItem()
        links = response.css('.a-link-normal.a-text-normal').css('::attr(href)').extract()
        #clean = [re.sub(r"$ref", "", item) for item in links]
        l1 = []
        for l in links:
            if (l.startswith('/Bosch')) and ('https://amazon.in'+l not in l1):
                l1.append('https://amazon.in'+l)
        items['links'] = l1


        yield items