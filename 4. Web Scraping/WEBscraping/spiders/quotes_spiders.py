import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quote"
    start_urls = [
        "https://bluelimelearning.github.io/my-fav-quotes/"
    ]

    def parse(self, response):
        for quote in response.css('div.quotes'):
            yield {
                'quote':quote.css('p.aquote::text').extract(),
                'aquote':quote.css('p.author::text').extract_first(),
            }
