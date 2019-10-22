# -*- coding: utf-8 -*-
import scrapy
from PaaPa.items import PaapaItem
import ipdb

class ShanghaiSpider(scrapy.Spider):
    name = 'shanghai'
    allowed_domains = ['zjw.sh.gov.cn']
    start_urls = ['http://zjw.sh.gov.cn/zjw/sgs/index.html']
    
    def start_requests(self):
        for i in range(2,28):
            self.start_urls.append('http://zjw.sh.gov.cn/zjw/sgs/index_{}.html'.format(i))
        for url in self.start_urls:
            yield scrapy.Request(url,self.parse)

    def parse(self, response):
        for i in range(1,16):
            item=PaapaItem()
            sub_selector=response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div/ul/li[{}]'.format(i))
            title=sub_selector.xpath('./a/text()').extract()[0]
            item['title']=title
            url=sub_selector.xpath('./a/@href').extract()[0]
            item['url']="http://zjw.sh.gov.cn"+url
            date=sub_selector.xpath('./span/text()').extract()[0]
            item['date']=date
            ipdb.set_trace()
            yield(item)


