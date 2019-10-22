import unittest
import betamax
import requests
from scrapy.http import HtmlResponse

from PaaPa.spiders.shanghai import ShanghaiSpider


class MyTestCase(unittest.TestCase):
    def test_something(self):
        shSpider = ShanghaiSpider()
        self.assertEqual(False, False)

    def test_betamax(self):
        CASSETTE_LIBRARY_DIR = 'd:\\Project\\PaaPa\\tests\\responses'
        session = requests.Session()
        recorder = betamax.Betamax(
            session, cassette_library_dir=CASSETTE_LIBRARY_DIR
        )
        spider = ShanghaiSpider()
        with recorder.use_cassette('shanghai'):
            url = 'http://zjw.sh.gov.cn/zjw/sgs/index.html'
            response = session.get(url)
            scrapy_response = HtmlResponse(body=response.content, url=url)
            # spider.start_requests()
            result = spider.parse(scrapy_response)
            expect_company1={'date': '2019.07.11',
                             'title': '对中设建工集团有限公司的行政处罚决定书',
                             'url': 'http://zjw.sh.gov.cn/zjw/sgs/20190711/70450.html'}

            expect_company2={'date': '2019.05.28',
                             'title': '对上海朗擎建筑工程有限公司的行政处罚决定书',
                             'url': 'http://zjw.sh.gov.cn/zjw/sgs/20190528/69079.html'}
            expect_company3={'date': '2019.01.24',
                             'title': '对上海颐东机械施工工程有限公司的行政处罚决定书',
                             'url': 'http://zjw.sh.gov.cn/zjw/sgs/20190228/59348.html'}
            print(result)
            self.assertIn(expect_company1,result)
            self.assertIn(expect_company2,result)
            # self.assertIn(expect_company3,result)


if __name__ == '__main__':
    unittest.main()
