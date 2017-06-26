class DoubanxiaoshuoItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    pass
