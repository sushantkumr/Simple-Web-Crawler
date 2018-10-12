import unittest
from crawler import Crawler


class TestIsUrlInvalid(unittest.TestCase):

    def test_crawler(self):
        url = 'https://mix.com/'
        depth = 15
        obj = Crawler(url, depth)
        self.assertEqual(15, len(obj.crawled_urls))

    def test_crawler_empty_link(self):
        url = ''
        depth = 15
        obj = Crawler(url, depth)
        self.assertEqual(0, len(obj.crawled_urls))