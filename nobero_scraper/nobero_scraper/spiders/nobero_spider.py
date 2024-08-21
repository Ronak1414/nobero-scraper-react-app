import scrapy

class NoberoSpider(scrapy.Spider):
    name = "nobero_spider"
    start_urls = ['https://nobero.com/pages/men']

    def parse(self, response):
        category_links = response.css('.category-link::attr(href)').getall()
        for link in category_links:
            yield response.follow(link, callback=self.parse_category)
    
    def parse_category(self, response):
        product_links = response.css('.product-item a::attr(href)').getall()
        for link in product_links:
            yield response.follow(link, callback=self.parse_product)
    
    def parse_product(self, response):
        product = {
            "category": response.css('.breadcrumb .active::text').get(),
            "url": response.url,
            "title": response.css('.product-title h1::text').get(),
            "price": response.css('.price .current::text').get(),
            "MRP": response.css('.price .was::text').get(),
            "last_7_day_sale": response.css('.price .discount::text').get(),
            "available_skus": self.parse_skus(response),
            "fit": response.css('.product-specs .fit::text').get(),
            "fabric": response.css('.product-specs .fabric::text').get(),
            "neck": response.css('.product-specs .neck::text').get(),
            "sleeve": response.css('.product-specs .sleeve::text').get(),
            "pattern": response.css('.product-specs .pattern::text').get(),
            "length": response.css('.product-specs .length::text').get(),
            "description": response.css('.product-description::text').get()
        }
        yield product

    def parse_skus(self, response):
        skus = []
        colors = response.css('.product-variants .color-option::attr(data-color)').getall()
        for color in colors:
            sizes = response.css(f'.size-{color} .size-option::text').getall()
            skus.append({
                "color": color,
                "size": sizes
            })
        return skus
