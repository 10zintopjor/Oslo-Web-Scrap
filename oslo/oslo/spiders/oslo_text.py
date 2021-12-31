import scrapy


class OsloTextSpider(scrapy.Spider):
    name = 'oslo_text'
    allowed_domains = ['https://www2.hf.uio.no/polyglotta/index.php?page=library&bid=2']
    start_urls = ['https://www2.hf.uio.no/polyglotta/index.php?page=library&bid=2']

    def parse(self, response):
        ul = response.css('ul')
        li = ul.css('li')


        for link in li:
            item = {
            'name' : link.css('a::text').get(),
            'ref' : link.css('a::attr(href)').get()
            }
            yield response.follow(link.css('a::attr(href)').get(),callback=self.parse_links)

    def parse_links(self,response):
        sidebar = response.css('div.venstrefelt')
        tr = sidebar.css('tr')
        for a in tr:
            item 
        