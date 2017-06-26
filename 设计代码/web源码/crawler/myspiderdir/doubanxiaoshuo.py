# -*- coding: utf-8 -*-
import scrapy
from ${projectName}.items import DoubanxiaoshuoItem
from scrapy.selector import Selector
from scrapy.http import Request

class Spider(scrapy.Spider):
	name = 'doubanxiaoshuo'
	allowed_domains = ['book.douban.com']
	start_urls = [u'https://book.douban.com/tag/%e5%b0%8f%e8%af%b4']


	def parse(self,response):
		
		selector = Selector(response)
		item = DoubanxiaoshuoItem()
		books = response.xpath('//ul[@class="subject-list"]/li[@class="subject-item"]')
		for info in books:			
			item['name'] = info.xpath('div[@class="info"]/h2/a/@title').extract()
			item['author'] =  info.xpath('div[@class="info"]/div[@class="pub"]/text()').extract()[0].strip() 
			item['url'] = info.xpath('div[@class="info"]/h2/a/@href').extract()
			item['score'] = info.xpath('div//span[@class="rating_nums"]/text()').extract()
			yield item
		next_url = response.xpath('//span[@class="next"]/a/@href').extract()[0]
		if next_url:
			yield Request(url="https://book.douban.com/"+next_url,callback=self.parse)