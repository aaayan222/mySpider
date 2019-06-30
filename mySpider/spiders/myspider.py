# -*- coding: utf-8 -*-
import scrapy

from mySpider.items import MyspiderItem


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['12365auto.com']
    start = 1
    start_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-'
    start_urls = [start_url+str(start)+'.shtml']

    def parse(self, response):

        item = MyspiderItem()
        for i in response.xpath('//div[@class="tslb_b"]//tr[1]/following-sibling::*'):
            item['brand'] = i.xpath('.//td[2]/text()').extract()
            item['line']= i.xpath('.//td[3]/text()').extract()
            item['car'] = i.xpath('.//td[4]/text()').extract()
            item['details'] = i.xpath('.//td[5]//text()').extract()
            item['problems'] = i.xpath('.//td[6]/text()').extract()
            item['date'] = i.xpath('.//td[7]/text()').extract()

            # items = {
            #     'brand': item['brand'][0],
            #     'line': item['line'][0],
            #     'car': item['car'][0],
            #     'details': item['details'][0],
            #     'problems': item['problems'][0],
            #     'date': item['date'][0]
            # }

            yield item


        for i in range(2,3):
            url = self.start_url + str(i) + '.shtml'
            yield scrapy.Request(url, callback=self.parse)

        # if self.start < 3:
        #     self.start += 1
        #     url = self.start_url + str(self.start)+'.shtml'
        #     yield scrapy.Request(url=url,callback=self.parse)