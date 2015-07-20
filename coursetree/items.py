# -*- coding: utf-8 -*-

import scrapy

class SubjectsItem(scrapy.Item):
    description = scrapy.Field()
    code = scrapy.Field()
    url = scrapy.Field()
    pass
