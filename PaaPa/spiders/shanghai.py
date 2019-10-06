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
            sub_selector=response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div/ul/li[{}]'.format(i))
            title=sub_selector.xpath('./a/text()').extract()[0]
            item['title']=title
            url=sub_selector.xpath('./a/@href').extract()[0]
            item['url']="http://zjw.sh.gov.cn"+url
            date=sub_selector.xpath('./span/text()').extract()[0]
            item['date']=date
            items.append(item)
        print(items)
        return items

