import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.http import HtmlResponse
import time

class LinkSpider(CrawlSpider):
    name = 'link_spider'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_with_selenium', follow=True),
    )

    def __init__(self, *args, **kwargs):
        super(LinkSpider, self).__init__(*args, **kwargs)
        self.visited_urls = set()

        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Remove this line if you want to see the browser
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def parse_item(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.add(response.url)
            # Scrape data from the page
            if 'category' in response.url:
                yield self.parse_category(response)
            elif 'product' in response.url:
                yield self.parse_product(response)
            else:
                yield self.parse_generic(response)

    def parse_start_url(self, response):
        return self.parse_with_selenium(response)

    def parse_with_selenium(self, response):
        self.driver.get(response.url)
        time.sleep(5)  # Wait for the page to load

        # Check for CAPTCHA and handle manually
        if "captcha" in self.driver.page_source.lower():
            self.handle_captcha()

        body = self.driver.page_source
        new_response = HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=response)
        return self.parse_item(new_response)

    def handle_captcha(self):
        print("CAPTCHA detected. Please solve it manually in the browser.")
        while True:
            input("Press Enter after solving the CAPTCHA manually...")
            self.driver.refresh()
            time.sleep(5)  # Give time for the page to refresh
            if "captcha" not in self.driver.page_source.lower():
                break

    def parse_generic(self, response):
        yield {
            'url': response.url,
            'title': response.css('title::text').get(),
            'paragraphs': response.css('p::text').getall(),
        }

    def parse_category(self, response):
        yield {
            'url': response.url,
            'category_name': response.css('h1::text').get(),
            'subcategories': response.css('.subcategory::text').getall(),
        }

    def parse_product(self, response):
        yield {
            'url': response.url,
            'product_name': response.css('h1::text').get(),
            'price': response.css('.price::text').get(),
            'description': response.css('.description::text').get(),
        }

    def closed(self, reason):
        self.driver.quit()
