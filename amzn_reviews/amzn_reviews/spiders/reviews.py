import scrapy


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'
    base_url = "https://www.amazon.in/Bosch-Fully-Automatic-Loading-Washing-WAT24464IN/product-reviews/B07DZTF6KC/ref=cm_cr_getr_d_paging_btm_prev_3?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber="
    start_urls = []

    for i in range(1,4):
        start_urls.append(base_url + str(i))

    def parse(self, response):

        rating = response.css('#cm_cr-review_list .review-rating')
        date = response.css('#cm_cr-review_list .review-date')
        title = response.css('.review-title')
        review = response.css('.review-text')


        count = 0
        for r in rating:
            yield {'Rating': ''.join(r.xpath('.//text()').extract()).replace(' out of 5 stars', ''),
                   'Date': ''.join(date[count].xpath(".//text()").extract()).strip('Reviewed in India on '),
                   'Title': ''.join(title[count].xpath(".//text()").extract()).strip(),
                   'Review': ''.join(review[count].xpath(".//text()").extract()).strip()
                   }
            count = count + 1

