https://docs.scrapy.org/en/latest/intro/tutorial.html#our-first-spider

##How to run
//scrapy crawl {the name of the spider}
>> scrapy crawl quotes
this command creates 2 html files since we provided 2 urls in the QuotesSpider class
and we set the parse method to create a file to save the response body for each urls
we provided