# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from todayMoive.items import TodaymoiveItem


class WuhanmovespiderSpider(scrapy.Spider):

    name = 'wuHanMoveSpider'
    source='上海市住房和城乡建设管理委员会'
    # allowed_domains = ['jycinema.com']
    start_urls = ('http://zjw.sh.gov.cn/zjw/sgs/index.html',)

    # def start_requests(self):
    #     for i in range(2,28):
    #         self.start_urls.append('http://zjw.sh.gov.cn/zjw/sgs/index_{}.html'.format(i))
    #     for url in self.start_urls:
    #         yield Request(url,callback=self.parse)

    def parse(self, response):
        items=[]
        for i in range(1,16):
            sub=response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div/ul/li[{}]/a/text()'.format(i))
            item=TodaymoiveItem()
            item['movieName']=sub.extract()
            items.append(item)
        return items