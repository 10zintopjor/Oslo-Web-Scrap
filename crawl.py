import scrapy
from scrapy.crawler import CrawlerProcess

class OsloSpider(scrapy.Spider):
    name="oslo"

    def start_requests(self):
        yield scrapy.Request('https://www2.hf.uio.no/polyglotta/index.php?page=library&bid=2')

    def parse(self,response):
        ul = response.css('ul')
        li = ul.css('li')


        for link in li:
            item = {
            'name' : link.css('a::text').get(),
            'ref' : link.css('a::attr(href)').get()
            }

            #yield item
            yield response.follow(link.css('a::attr(href)').get(),callback=self.parse_links)  


    def parse_links(self,response):
        sidebar = response.css('div.venstrefelt')
        tr = sidebar.css('tr')
        for a in tr:
            items = {
                'chapter': a.css('a::text').get().strip("\n"),
                'ref' :a.css('a::attr(href)').get().strip("\n")
            } 
            yield items



process = CrawlerProcess(settings = {
    'FEED_URI':'output.csv',
    'FEED_FORMAT':'csv'
})
process.crawl(OsloSpider)
process.start()