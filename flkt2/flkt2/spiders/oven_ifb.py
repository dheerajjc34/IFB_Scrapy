import scrapy
from ..items import Flkt2Item

class WashIfbSpider(scrapy.Spider):
    name = 'oven_ifb'
    #allowed_domains = ['flipkart.com']
    start_urls = [
      "https://flipkart.com/ifb-23-l-convection-microwave-oven/p/itmdwmvzgvtbzcnz?pid=MRCDWK8TTHVHW3WY&lid=LSTMRCDWK8TTHVHW3WYAU7NOA&marketplace=FLIPKART&srno=b_1_1&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCDWK8TTHVHW3WY.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-25-l-convection-microwave-oven/p/itmef2ztgtew4cnz?pid=MRCEF2ZSV7RPRVHK&lid=LSTMRCEF2ZSV7RPRVHKNPKABY&marketplace=FLIPKART&srno=b_1_2&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCEF2ZSV7RPRVHK.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-17-l-grill-microwave-oven/p/itmef2zthcxgpmjg?pid=MRCEF2ZSRFPC4PPB&lid=LSTMRCEF2ZSRFPC4PPBIJRMIL&marketplace=FLIPKART&srno=b_1_3&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCEF2ZSRFPC4PPB.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-20-l-convection-microwave-oven/p/itmdwmvzxgbcdvg9?pid=MRCDWK8TMQCEGTYK&lid=LSTMRCDWK8TMQCEGTYKHQSFZU&marketplace=FLIPKART&srno=b_1_4&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCDWK8TMQCEGTYK.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-17-l-solo-microwave-oven/p/itmdwmvzxdz26gen?pid=MRCDWK8TG5YAU33Z&lid=LSTMRCDWK8TG5YAU33Z6BW2QL&marketplace=FLIPKART&srno=b_1_5&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCDWK8TG5YAU33Z.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-20-l-solo-microwave-oven/p/itmeftrw5s52ywbg?pid=MRCEFTRWCDUYJQTE&lid=LSTMRCEFTRWCDUYJQTE12BSG0&marketplace=FLIPKART&srno=b_1_6&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCEFTRWCDUYJQTE.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-20-l-convection-microwave-oven/p/itmef3kdfhkc4zug?pid=MRCEF3KDVTDQP69D&lid=LSTMRCEF3KDVTDQP69DXN7SQH&marketplace=FLIPKART&srno=b_1_7&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCEF3KDVTDQP69D.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-17-l-solo-microwave-oven/p/itmeftrwhehgk6xg?pid=MRCEFTRWCGZ3B2RC&lid=LSTMRCEFTRWCGZ3B2RCR4JPWD&marketplace=FLIPKART&srno=b_1_8&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCEFTRWCGZ3B2RC.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-20-l-convection-microwave-oven/p/itmfhyzgvzdkspzc?pid=MRCFHYZGTYYU6DAC&lid=LSTMRCFHYZGTYYU6DACTHZCXD&marketplace=FLIPKART&srno=b_1_9&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCFHYZGTYYU6DAC.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-30-l-convection-microwave-oven/p/itmfhyzgaexgyxfa?pid=MRCFHYZGFYCJCJWG&lid=LSTMRCFHYZGFYCJCJWGJXUD8E&marketplace=FLIPKART&srno=b_1_10&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCFHYZGFYCJCJWG.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-20-l-convection-grill-microwave-oven/p/itm07246844c5c57?pid=MRCFP6WMBCNRNP8J&lid=LSTMRCFP6WMBCNRNP8JSXOAZE&marketplace=FLIPKART&srno=b_1_11&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCFP6WMBCNRNP8J.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-30-l-convection-microwave-oven/p/itmdwmvzzshqwrhs?pid=MRCF8H3JZ23WHSAT&lid=LSTMRCF8H3JZ23WHSATLZPODY&marketplace=FLIPKART&srno=b_1_12&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCF8H3JZ23WHSAT.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-23-l-convection-microwave-oven/p/itmef2ztequxvqa9?pid=MRCEF2ZSTQU9QBHT&lid=LSTMRCEF2ZSTQU9QBHTYJS6N7&marketplace=FLIPKART&srno=b_1_13&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCEF2ZSTQU9QBHT.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-25-l-convection-microwave-oven/p/itmef2zteehmrvwq?pid=MRCEF2ZS7FGDSYKM&lid=LSTMRCEF2ZS7FGDSYKMFJKMBH&marketplace=FLIPKART&srno=b_1_14&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCEF2ZS7FGDSYKM.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-20-l-convection-microwave-oven/p/itmfaja48z6yr8md?pid=MRCFAJA49URG5CCC&lid=LSTMRCFAJA49URG5CCCJXUPDC&marketplace=FLIPKART&srno=b_1_15&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCFAJA49URG5CCC.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-20-l-grill-microwave-oven/p/itmeftrwxravzfzf?pid=MRCEFTRWHGRWAXMT&lid=LSTMRCEFTRWHGRWAXMTQMHL9V&marketplace=FLIPKART&srno=b_1_16&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCEFTRWHGRWAXMT.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-25-l-convection-microwave-oven/p/itmeftrwma66wgp9?pid=MRCEFTRWR7ZQA43Q&lid=LSTMRCEFTRWR7ZQA43QUTYURD&marketplace=FLIPKART&srno=b_1_17&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCEFTRWR7ZQA43Q.SEARCH&ssid=c33esi66gw0000001596633672562",
      "https://flipkart.com/ifb-25-l-convection-microwave-oven/p/itmdwmvzgpkh59xw?pid=MRCDWK8TFQFJ3R2Z&lid=LSTMRCDWK8TFQFJ3R2ZUPTRAU&marketplace=FLIPKART&srno=b_1_18&otracker=CLP_Filters&fm=organic&iid=f945d563-fab2-46af-8cf9-03b47d1feb44.MRCDWK8TFQFJ3R2Z.SEARCH&ssid=c33esi66gw0000001596633672562"
    ]

    def parse(self, response):
        items = Flkt2Item()
        product_name = response.css('._35KyD6::text').extract()
        product_rating = response.css('._1i0wk8').css('::text').extract()
        product_price = response.css('._3qQ9m1').css('::text').extract()
        no_ratings = response.css('._2yc1Qo:nth-child(2) span').css('::text').extract()
        highlights = response.css('.g2dDAR').css('::text').extract()
        prod_desc = response.css('._2THx53').css('::text').extract()
        gen_spec = response.css('._2RngUh').css('::text').extract()
        perf_feat = response.css('._2RngUh:nth-child(4)').css('::text').extract()
        cook_feat = response.css('._2RngUh:nth-child(5)').css('::text').extract()
        body_feat = response.css('._2RngUh:nth-child(6)').css('::text').extract()
        conv_feat = response.css('._2RngUh:nth-child(7)').css('::text').extract()
        pow_feat = response.css('._2RngUh:nth-child(8)').css('::text').extract()
        add_feat = response.css('._2RngUh:nth-child(9)').css('::text').extract()
        dimensions = response.css('._2RngUh:nth-child(10)').css('::text').extract()

        #cleaning
        prices = [item.strip('\u20b9') for item in product_price]
        ratings = [item.strip(' Ratings &') for item in no_ratings]
        #highlights2 = [item.replace('Highlights, ','') for item in highlights]

        items['product_name'] = product_name
        items['product_rating'] = product_rating
        items['product_price'] = prices
        items['no_ratings'] = ratings
        items['highlights'] = highlights
        items['prod_desc'] = prod_desc
        items['gen_spec'] = gen_spec
        items['perf_feat'] = perf_feat
        items['cook_feat'] = cook_feat
        items['body_feat'] = body_feat
        items['conv_feat'] = conv_feat
        items['pow_feat'] = pow_feat
        items['add_feat'] = add_feat
        items['dimensions'] = dimensions

        yield items
