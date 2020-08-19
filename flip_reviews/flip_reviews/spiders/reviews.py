import scrapy


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'
    base_url = "https://www.flipkart.com/lg-7-kg-5-star-fully-automatic-front-load-in-built-heater-silver/product-reviews/itm1fb6b04b9570d?pid=WMNFTPBYJM57XG5G&aid=overall&certifiedBuyer=false&sortOrder=MOST_RECENT&page="
    start_urls = []

    for i in range(1,6):
        start_urls.append(base_url + str(i))

    def parse(self, response):
        rating = response.css('.E_uFuv')
        title = response.css('._2xg6Ul')
        review = response.css('.qwjRop')

        count = 0
        for r in rating:
            yield {'Rating': ''.join(r.xpath('.//text()').extract()),
                   'Title': ''.join(title[count].xpath(".//text()").extract()),
                   'Review': ''.join(review[count].xpath(".//text()").extract()).strip('READ MORE').replace('<br>',' ')
            }
            count = count + 1
