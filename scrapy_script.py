import scrapy
REQUEST_FINGERPRINTER_IMPLEMENTATION = 'scrapy.utils.request.request_fingerprint_sha1'

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://art-of-fullstack.net']
    print(start_urls)
    print('hello world')
    def parse(self, response):
        print('HELLO', response)
            for quote in response.css('.services'):
                print(quote, 'hello')
   	
print('end')

