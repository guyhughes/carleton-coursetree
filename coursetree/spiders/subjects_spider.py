import scrapy

from coursetree.items import SubjectsItem
class SubjectsSpider(scrapy.Spider):
    name = "subjects"
    allowed_domains = ["carleton.ca"]
    start_urls = [ "http://calendar.carleton.ca/undergrad/courses/" ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="course"]/p/a'):
            item = SubjectsItem()
            item['code'] = sel.xpath('text()').extract()[0]
            item['url'] = response.urljoin(sel.xpath('@href').extract()[0])
            item['description'] = sel.xpath('preceding-sibling::text()[1]').re("[A-z\'\ ]{3,}(?![\ ]+\()")[0]
            # print code, url, description
            yield item

