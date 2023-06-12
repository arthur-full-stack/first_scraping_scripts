import scrapy


class MySpider(scrapy.Spider):
    name = "myspider"
    base_url = "https://ss.ge/en/real-estate/l/Flat?Page={}&RealEstateTypeId=5&PriceType=false&CurrencyId=1"
    index = 1
    add_index = 1

    def start_requests(self):
        yield scrapy.Request(url=self.base_url.format(1), callback=self.all_requests)

    def all_requests(self, response):
        last_page = response.css(".last a::text").get()
        urls = [self.base_url.format(page) for page in range(1, int(last_page) + 1)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        text_nodes = response.css(".latest_article_each *::text").getall()
        image_links = response.css("img[data-src]::attr(data-src)").getall()

        cleaned_text = [text.strip() for text in text_nodes if text.strip()]
        extracted_text = " ".join(cleaned_text)
        with open(f"../../scraped_data_page{self.index}.txt", "a") as file:
            for link in image_links:
                file.write(link + "\n")
            file.write(extracted_text + "\n")
        self.index += 1

        active_links = response.css(".listing-carousel a::attr(href)").getall()
        for link in active_links:
            yield response.follow(url=link, callback=self.parse_additional_info)
        self.add_index = 1

    def parse_additional_info(self, response):
        additional_info = response.css(".detailed_article_body *::text").getall()
        cleaned_text = [text.strip() for text in additional_info if text.strip()]
        extracted_text = " ".join(cleaned_text)
        with open(
            f"../../additional_info{self.index}.{self.add_index}.txt", "a"
        ) as file:
            file.write(extracted_text + "\n")
        self.add_index += 1
