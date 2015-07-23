import scrapy

from coursetree.items import CoursesItem
import re

class CoursesSpider(scrapy.Spider):
    name = "courses"
    allowed_domains = ["carleton.ca"]

    # TODO: this is a param
    start_urls = [ "http://calendar.carleton.ca/undergrad/courses/COMP/" ]

    def parse(self, response):
        for course in response.xpath('//div[@id="courseinventorycontainer"]/div/div[@class="courseblock"]'):
            item = CoursesItem()
            item['code'] = course.xpath('strong/text()').re('[A-Z]{4}\s[0-9]{4}')
            item['credit'] = course.xpath('strong/text()').re('[0-9]{1,2}\.[0-9]{1,2}')
            item['title'] = course.xpath('strong/text()[preceding-sibling::br]').re('[A-z\ \'\&0-9]*$')[0]
            item['description'] = course.xpath('div[@class="coursedescadditional"]/preceding-sibling::text()').extract()
            
            item['also_listed_as'] = course.xpath('div[@class="coursedescadditional"]/text()[contains(.,"Also listed as")]/following-sibling::a[1]/text()').extract()
            
            item['precludes_credit_for'] = course.xpath('div[@class="coursedescadditional"]/text()[contains(.,"Precludes additional credit for")]/following-sibling::br[1]/preceding-sibling[1]').extract() 

            item['prerequisites'] = course.xpath('div[@class="coursedescadditional"]/text()[contains(.,"Prerequisite")]/following-sibling::a/text()').extract() #.re('[A-Z]{4}\s[0-9]{4}')

            print item
            yield item
