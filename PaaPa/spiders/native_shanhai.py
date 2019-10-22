# -*- coding: utf-8 -*-
import scrapy
from PaaPa.items import PaapaItem
from lxml import etree
import ipdb

class NativeShanhaiSpider(scrapy.Spider):
    name = 'native_shanhai'
    allowed_domains = ['zjw.sh.gov.cn']
    start_urls = ['http://zjw.sh.gov.cn/zjw/sgs/index.html']
    
    def start_requests(self):
        for i in range(2,28):
            self.start_urls.append('http://zjw.sh.gov.cn/zjw/sgs/index_{}.html'.format(i))
        for url in self.start_urls:
            yield scrapy.Request(url,self.parse)

    def parse(self,response):
        item=PaapaItem()
        content=etree.HTML(response.text)
        # ipdb.set_trace()
        for i in range(1,16):
            title=''.join(content.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div/ul/li[{}]/a//text()'.format(i))).strip()
            if title:
                item['title']=title
                url=''.join(content.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div/ul/li[{}]/a/@href'.format(i))).strip()
                item['url']="http://zjw.sh.gov.cn"+url
                get_date=''.join(content.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div/ul/li[{}]/span//text()'.format(i))).strip()
                item['date']=get_date
                yield item




