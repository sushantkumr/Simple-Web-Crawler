import unittest
from crawler import Crawler
from helpers import check_if_invalid, url_clean_up


class CrawlerTests(unittest.TestCase):

    def test_check_if_invalid_with_pdf(self):
        link = 'https://www.dropbox.com/s/SomeDocument.pdf'
        truth_value = check_if_invalid(link)
        self.assertTrue(truth_value)

    def test_check_if_invalid_with_docx(self):
        link = 'https://www.dropbox.com/s/SomeDocument.docx'
        truth_value = check_if_invalid(link)
        self.assertTrue(truth_value)

    def test_check_if_invalid_mailing_link(self):
        link = 'mailto:abcd@example.com'
        truth_value = check_if_invalid(link)
        self.assertTrue(truth_value)

    def test_check_if_invalid_empty_link(self):
        link = ''
        truth_value = check_if_invalid(link)
        self.assertTrue(truth_value)

    def test_check_if_invalid_fragments(self):
        valid_link = 'https://www.google.com/#about_us'
        truth_value = check_if_invalid(valid_link)
        self.assertTrue(truth_value)

    def test_check_if_invalid_failure(self):
        valid_link = 'https://www.google.com'
        truth_value = check_if_invalid(valid_link)
        self.assertFalse(truth_value)

    def test_url_clean_up_relative_url(self):
        link = '/homepage'
        parent_url = 'https://www.mixup.com'
        complete_url = url_clean_up(parent_url, link)
        self.assertEqual('https://www.mixup.com/homepage', complete_url)

    def test_url_clean_up_remove_slashes(self):
        link = '//homepage'
        parent_url = 'https://www.mixup.com'
        complete_url = url_clean_up(parent_url, link)
        self.assertEqual('https://www.mixup.com/homepage', complete_url)

    def test_url_clean_up_remove_no_http(self):
        link = '/homepage/'
        parent_url = 'www.mixup.com/'
        complete_url = url_clean_up(parent_url, link)
        self.assertEqual('http://www.mixup.com/homepage', complete_url)

    def test_url_clean_up_remove_trailing_slash(self):
        link = '/homepage/'
        parent_url = 'https://www.mixup.com/'
        complete_url = url_clean_up(parent_url, link)
        self.assertEqual('https://www.mixup.com/homepage', complete_url)

    def test_url_clean_up_remove_empty_link(self):
        parent_url = 'https://www.mixup.com/'
        complete_url = url_clean_up(parent_url, '')
        self.assertEqual('https://www.mixup.com', complete_url)

    def test_crawler(self):
        url = 'https://mix.com/'
        depth = 1000
        obj = Crawler(url, depth)
        self.assertEqual(1000, len(obj.crawled_urls))

    def test_crawler_empty_link(self):
        url = ''
        depth = 1000
        obj = Crawler(url, depth)
        self.assertEqual(0, len(obj.crawled_urls))


if __name__ == '__main__':
    unittest.main()
