# -*- coding: utf-8 -*-
#author zhangr
#thanks to Lving
import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import request, Request
from scrapy.selector import Selector
from ${projectName}.items import LoveFoodItem  #引入items中的类


class Food(CrawlSpider):
    name = "foodspider"
    start_urls = ['http://www.dianping.com/search/category/25/10']
    url = 'http://www.dianping.com/search/category/25/10'

    def parse(self, response):
        item = LoveFoodItem() #所有的网页数据
        selector = Selector(response)
        Foods = selector.xpath('//*[@id="shop-all-list"]/ul/li')
        for eachFood in Foods:
            restaurant = eachFood.xpath('div[2]/div[1]/a/h4/text()').extract()
            star = eachFood.xpath('div[2]/div[2]/span/@title').extract()
            average_price = eachFood.xpath('div[2]/div[2]/a[2]/b/text()').extract()
            foodtype = eachFood.xpath('div[2]/div[3]/a[1]/span/text()').extract()
            addr = eachFood.xpath('div[2]/div[3]/a[2]/span/text()').extract()
            if restaurant:
                item['restaurant'] = restaurant[0]
            else:
                item['restaurant'] = None
            if star:
                item['star'] = star[0]
            else:
                item['star'] = None
            if average_price:
                item['average_price'] = average_price[0]
            else:
                item['average_price'] = None
            if foodtype:
                item['foodtype'] = foodtype[0]
            else:
                item['foodtype'] = None
            if addr:
                item['addr'] = addr[0]
            else:
                item['addr'] = None

            yield item
        nextpage = selector.xpath('//*[@id="top"]/div[6]/div[3]/div[1]/div[2]/a/@href').extract()[-1]
        # nextpage 的标签容易出现变动
        # //*[@id="top"]/div[6]/div[3]/div[1]/div[2]/a[11] page1
        # //*[@id="top"]/div[6]/div[3]/div[1]/div[2]/a[12] page2
        # //*[@id="top"]/div[6]/div[3]/div[1]/div[2]/a[12] page3
        if nextpage:
            # 字符串切片 拼接
            nextpage = nextpage[22:]
            yield Request(self.url+nextpage, callback=self.parse)
