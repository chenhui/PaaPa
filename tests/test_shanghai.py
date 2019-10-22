import unittest
from PaaPa.spiders import shanghai

class ShanghaiSpiderTest(unittest.TestCase):

    def setUp(self):
        self.spider = shanghai.ShanghaiSpider()

    def _test_item_results(self, results, expected_length):
        count = 0
        permalinks = set()
        for item in results:
            self.assertIsNotNone(item['content'])
            self.assertIsNotNone(item['title'])
        self.assertEqual(count, expected_length)