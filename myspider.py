from __future__ import unicode_literals

import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        # for every h2 elements with `entry-title` css class get the first
        # result
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}
        # find the next link (paginator) element
        next_page = response.css(
            'div.prev-post > a ::attr(href)').extract_first()
        # if next link exist then do the parse again using the newly acquired
        # link
        if next_page:
            yield scrapy.Request(response.urljoin(next_page),
                                 callback=self.parse)
