# -*- coding: utf-8 -*-
import scrapy
from PaaPa.items import PaapaItem
import ipdb

class ShanghaiSpider(scrapy.Spider):
    name = 'shanghai'
    allowed_domains = ['zjw.sh.gov.cn']
    start_urls = ['http://zjw.sh.gov.cn/zjw/sgs/index.html']

    def parse(self, response):
        # file="shanghai.html"
        # with open(file,'wb') as f:
        #     str=response.body
        #     f.write(str)
        # i=1
        # str=response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div/ul/li[{}]/a/text()'.format(i)).extract()[0]
        items=[]
        for i in range(1,16):
            item=PaapaItem()
            gonshi=response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div/ul/li[{}]/a/text()'.format(i)).extract()[0]
            # ipdb.set_trace()
            item['gongShiFile']=gonshi
            items.append(item)
        print(items)
        return items

