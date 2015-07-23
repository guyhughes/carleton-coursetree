# -*- coding: utf-8 -*-

import scrapy

class SubjectsItem(scrapy.Item):
    description = scrapy.Field()
    code = scrapy.Field()
    url = scrapy.Field()
    pass

class CoursesItem(scrapy.Item):
    code = scrapy.Field()

    title = scrapy.Field()
    description = scrapy.Field()

    also_listed_as = scrapy.Field()
    precludes_credit_for = scrapy.Field()

    prerequisites = scrapy.Field()
    restrictions = scrapy.Field()
    
    credit = scrapy.Field()

    pass
    
