# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Amzn1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_rating = scrapy.Field()
    product_price = scrapy.Field()
    no_ratings = scrapy.Field()
    highlights = scrapy.Field()
    tech_details = scrapy.Field()
    prod_desc = scrapy.Field()

    pass

class AmznLinkItem(scrapy.Item):
    links = scrapy.Field()

    pass
