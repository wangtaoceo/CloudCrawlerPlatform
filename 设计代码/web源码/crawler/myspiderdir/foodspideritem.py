class LoveFoodItem(scrapy.Item):
    restaurant = scrapy.Field()
    star = scrapy.Field()
    average_price = scrapy.Field()
    foodtype = scrapy.Field()
    addr = scrapy.Field()
    pass
