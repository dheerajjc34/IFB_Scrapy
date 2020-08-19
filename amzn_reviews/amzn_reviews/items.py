# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmznReviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rating = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    review = scrapy.Field()
    pass
