import scrapy

class OsloSpider(scrapy.Spider):
    name = "oslo"
    start_urls = ['https://www2.hf.uio.no/polyglotta/index.php?page=library&bid=2']

    def parse(seld,response):
        