# -*- coding: utf-8 -*-
import scrapy
from ${projectName}.items import DoubandianyingItem
from scrapy.selector import Selector
from scrapy.http import Request

class Spider(scrapy.Spider):
	name = 'doubandianying'
	allowed_domains = ['movie.douban.com']
	start_urls = [u'https://movie.douban.com/tag/%E7%BE%8E%E5%9B%BD']


	def parse(self,response):
		
		selector = Selector(response)
		item = DoubandianyingItem()
		movie = response.xpath('//tr[@class="item"]')
		for info in movie:			
			item['name'] = info.xpath('td[1]/a/@title').extract()
			item['author'] = info.xpath('td[2]/div[@class="pl2"]/p/text()').extract()[0].strip() 
			item['url'] = info.xpath('td[2]/div[@class="pl2"]/a/@href').extract()
			item['score'] = info.xpath('td[2]/div[@class="pl2"]//span[@class="rating_nums"]/text()').extract()
			yield item
		next_url = response.xpath('//link[@rel="next"]/@href').extract()[0]
		if next_url:
			yield Request(url=next_url,callback=self.parse)