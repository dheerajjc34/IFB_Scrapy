import scrapy
from ..items import Amzn1Item

class WashIfbSpider(scrapy.Spider):
    name = 'wash_ifb'
    #allowed_domains = ['amazon.in']

    start_urls = [
      "https://amazon.in/Bosch-Convection-Microwave-HMB55C453X-Stainless/dp/B07DD5L54F/ref=sr_1_1?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-1",
      "https://amazon.in/Bosch-Convection-Microwave-HMB55C463X-Borosil/dp/B07DD1K7GX/ref=sr_1_2?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-2",
      "https://amazon.in/Bosch-Serie-Stainless-Microwave-BFL553MS0I/dp/B07PNNMDR5/ref=sr_1_3?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-3",
      "https://amazon.in/Bosch-Serie-built-oven-hotair/dp/B07Z253CL9/ref=sr_1_4?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-4",
      "https://amazon.in/Bosch-Serie-Stainless-Microwave-HMT75M551I/dp/B00BMKPHJQ/ref=sr_1_5?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-5",
      "https://amazon.in/Bosch-Pyrolitic-Built-Stainless-HBN574BR0Z/dp/B07MHDZ4W3/ref=sr_1_6?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-6",
      "https://amazon.in/Bosch-Built-Single-Stainless-HBN534BS0Z/dp/B07MP4V98W/ref=sr_1_7?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-7",
      "https://amazon.in/Bosch-Serie-Stainless-Steel-HBG633BS1J/dp/B00U8RJ75Y/ref=sr_1_8?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-8",
      "https://amazon.in/Bosch-BEL550MS0I-Stainless-Steel-Microwave/dp/B07M8GJKH2/ref=sr_1_9?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-9",
      "https://amazon.in/Bosch-Stainless-Digital-Automatic-Childproof/dp/B07TD2T99L/ref=sr_1_10?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-10",
      "https://amazon.in/Bosch-Display-Control-Built-Microwaves/dp/B07TD3J539/ref=sr_1_11?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-11",
      "https://amazon.in/Bosch-Built-Microwaves-Clock-Type/dp/B07TF4SD63/ref=sr_1_12?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-12",
      "https://amazon.in/Bosch-Distribution-Simultaneously-Electronic-Childproof/dp/B07TC1ZG9D/ref=sr_1_13?dchild=1&fst=as%3Aoff&qid=1596783564&refinements=p_89%3ABosch&rnid=3837712031&s=kitchen&sr=1-13"
    ]

    def parse(self, response):
        items = Amzn1Item()
        #scrape selectors
        product_name = response.xpath('//*[(@id = "productTitle")]/text()').extract()
        product_rating = response.css('.a-size-medium.a-color-base').css('::text').extract()
        product_price = response.xpath('//*[(@id = "priceblock_ourprice")]/text()').extract()
        no_ratings = response.xpath('//*[(@id = "acrCustomerReviewText")]/text()').extract()
        highlights = response.xpath('//*[(@id = "feature-bullets")]//*[contains(concat( " ", @class, " " ), concat( " ", "a-list-item", " " ))]/text()').extract()
        tech_details = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col1", " " ))]//td/text()').extract()
        prod_desc = response.css('.apm-top .a-spacing-mini').css('::text').extract()
        #cleaning text
        names = [item.strip('\n') for item in product_name]
        prices = [item.strip('\u20b9\xa0') for item in product_price]
        rating = [item.strip(' out of 5') for item in product_rating]
        no_rati = [item.strip(' ratings') for item in no_ratings]
        highl = [item.strip('\n') for item in highlights]
        prod = [item.replace('\n\n        ','') for item in prod_desc]
        prod2 = [item.replace('\n    ',' ') for item in prod]

        #writing
        items['product_name'] = names
        items['product_rating'] = rating
        items['product_price'] = prices
        items['no_ratings'] = no_rati
        items['highlights'] = highl
        items['tech_details'] = tech_details
        items['prod_desc'] = prod2


        yield items