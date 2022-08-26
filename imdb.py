
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "imdb"
    start_urls=["https://www.imdb.com/chart/top/"]
    def parse(self,response):
        for content in response.xpath("//*[@id='main']/div/span/div/div/div[3]/table/tbody/tr"):
            yield{
                "headline" : content.xpath('td[2]/a/text()').get(),
                "date" : content.xpath('td[2]/span/text()').get(),
                "rating" : content.xpath('td[3]/strong/text()').get()
                }
            next_page = response.xpath('').get()
            if next_page is not None:
                yield response.follow(next_page,callable = self.parse)
                
# TO CRAWL : scrapy crawl imdb -o imdb.json
# TO START A PROJECT : scrapy startproject tutorial
