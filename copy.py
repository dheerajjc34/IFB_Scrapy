import scrapy
from ..items import AmznReviewsItem

class ReviewsSpider(scrapy.Spider):
    name = 'reviews'
    base_url = "https://www.amazon.in/IFB-Fully-Automatic-TL-RDS-Aqua-Sparkling/product-reviews/B00WU9Z51I/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber="
    start_urls = []

    for i in range(1, 3):
        start_urls.append(base_url + str(i))

    def parse(self, response):
        items = AmznReviewsItem()
        #selectors
        rating = response.css('#cm_cr-review_list .review-rating::text').extract()
        date = response.css('#cm_cr-review_list .review-date::text').extract()
        title = response.css('.a-text-bold span').extract()
        review = response.css('.review-text-content span').extract()

        #cleaning
        rate = [item.strip(' out of 5') for item in rating]
        d = [item.strip('Reviewed in India on ') for item in date]
        #returning values
        items['rating'] = rate
        items['date'] = d
        items['title'] = title
        items['review'] = review
        #scraped_data = {}
        '''for x in rate:
            yield {'Rating': rate,
                   'Date': d,
                   'Title': title,
                   'Review': review
                   }'''
        yield items
