import scrapy
from ..items import Amzn1Item

class OvenIfbSpider(scrapy.Spider):
    name = 'oven_ifb'
    start_urls = [
        'https://www.amazon.in/IFB-Convection-Microwave-25SC3-Metallic/dp/B0085W15RC/ref=sr_1_1?dchild=1&keywords=ifb&qid=1596649475&rnid=3576079031&s=kitchen&sr=1-1',
        'https://www.amazon.in/IFB-Convection-Microwave-20SC2-Metallic/dp/B00A7PGI18/ref=sr_1_2?dchild=1&keywords=ifb&qid=1596649475&rnid=3576079031&s=kitchen&sr=1-2',
        'https://www.amazon.in/IFB-Convection-Microwave-25SC4-Metallic/dp/B00P1KGR8I/ref=sr_1_3?dchild=1&keywords=ifb&qid=1596649475&rnid=3576079031&s=kitchen&sr=1-3',
        'https://www.amazon.in/IFB-Microwave-17PM-MEC-White/dp/B006TQNOR0/ref=sr_1_4?dchild=1&keywords=ifb&qid=1596649475&rnid=3576079031&s=kitchen&sr=1-4',
        'https://www.amazon.in/IFB-Grill-Microwave-20PG4S-Silver/dp/B015AAV3PA/ref=sr_1_6?dchild=1&keywords=ifb&qid=1596649475&rnid=3576079031&s=kitchen&sr=1-6',
        'https://www.amazon.in/IFB-Convection-Microwave-25BCS1-Black/dp/B01D30K3SC/ref=sr_1_7?dchild=1&keywords=ifb&qid=1596649475&rnid=3576079031&s=kitchen&sr=1-7',
        'https://www.amazon.in/IFB-Convection-Microwave-23BC5-Black/dp/B07R8MF114/ref=sr_1_8?dchild=1&keywords=ifb&qid=1596649475&rnid=3576079031&s=kitchen&sr=1-8',
        'https://www.amazon.in/IFB-Microwave-25PM2S-IFBJ0-Silver/dp/B085V1JD27/ref=sr_1_9?dchild=1&keywords=ifb&qid=1596649475&rnid=3576079031&s=kitchen&sr=1-9'
    ]

    def parse(self, response):
        items = Amzn1Item()
        # scrape selectors
        product_name = response.xpath('//*[(@id = "productTitle")]/text()').extract()
        product_rating = response.css('.a-size-medium.a-color-base').css('::text').extract()
        product_price = response.xpath('//*[(@id = "priceblock_ourprice")]/text()').extract()
        no_ratings = response.xpath('//*[(@id = "acrCustomerReviewText")]/text()').extract()
        highlights = response.xpath(
            '//*[(@id = "feature-bullets")]//*[contains(concat( " ", @class, " " ), concat( " ", "a-list-item", " " ))]/text()').extract()
        tech_details = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "col1", " " ))]//td/text()').extract()
        prod_desc = response.css('.apm-top .a-spacing-mini').css('::text').extract()
        # cleaning text
        names = [item.strip('\n') for item in product_name]
        prices = [item.strip('\u20b9\xa0') for item in product_price]
        rating = [item.strip(' out of 5') for item in product_rating]
        no_rati = [item.strip(' ratings') for item in no_ratings]
        highl = [item.strip('\n') for item in highlights]
        prod = [item.replace('\n\n        ', '') for item in prod_desc]
        prod2 = [item.replace('\n    ', ' ') for item in prod]

        # writing
        items['product_name'] = names
        items['product_rating'] = rating
        items['product_price'] = prices
        items['no_ratings'] = no_rati
        items['highlights'] = highl
        items['tech_details'] = tech_details
        items['prod_desc'] = prod2

        yield items