import unittest
from helpers import get_clean_url


class TestGetCleanUrl(unittest.TestCase):

    def test_get_clean_url_relative_url(self):
        link = '/homepage'
        parent_url = 'https://www.mixup.com'
        complete_url = get_clean_url(parent_url, link)
        self.assertEqual('https://www.mixup.com/homepage', complete_url)

    def test_get_clean_url_remove_slashes(self):
        link = '//homepage'
        parent_url = 'https://www.mixup.com'
        complete_url = get_clean_url(parent_url, link)
        self.assertEqual('https://www.mixup.com/homepage', complete_url)

    def test_get_clean_url_remove_no_http(self):
        link = '/homepage/'
        parent_url = 'www.mixup.com/'
        complete_url = get_clean_url(parent_url, link)
        self.assertEqual('http://www.mixup.com/homepage', complete_url)

    def test_get_clean_url_remove_trailing_slash(self):
        link = '/homepage/'
        parent_url = 'https://www.mixup.com/'
        complete_url = get_clean_url(parent_url, link)
        self.assertEqual('https://www.mixup.com/homepage', complete_url)

    def test_get_clean_url_remove_empty_link(self):
        parent_url = 'https://www.mixup.com/'
        complete_url = get_clean_url(parent_url, '')
        self.assertEqual('https://www.mixup.com', complete_url)