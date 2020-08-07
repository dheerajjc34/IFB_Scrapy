# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Flkt2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_rating = scrapy.Field()
    product_price = scrapy.Field()
    no_ratings = scrapy.Field()
    highlights = scrapy.Field()
    prod_desc = scrapy.Field()
    gen_spec = scrapy.Field()
    perf_feat = scrapy.Field()
    cook_feat = scrapy.Field()
    body_feat = scrapy.Field()
    conv_feat = scrapy.Field()
    pow_feat = scrapy.Field()
    add_feat = scrapy.Field()
    dimensions = scrapy.Field()

    pass

class FlktLinkItem(scrapy.Item):
    links = scrapy.Field()

    pass
