import unittest
from helpers import is_url_valid


class TestIsUrlValid(unittest.TestCase):

    def test_is_url_valid_with_pdf(self):
        link = 'https://www.dropbox.com/s/SomeDocument.pdf'
        truth_value = is_url_valid(link)
        self.assertFalse(truth_value)

    def test_is_url_valid_with_docx(self):
        link = 'https://www.dropbox.com/s/SomeDocument.docx'
        truth_value = is_url_valid(link)
        self.assertFalse(truth_value)

    def test_is_url_valid_mailing_link(self):
        link = 'mailto:abcd@example.com'
        truth_value = is_url_valid(link)
        self.assertFalse(truth_value)

    def test_is_url_valid_empty_link(self):
        link = ''
        truth_value = is_url_valid(link)
        self.assertFalse(truth_value)

    def test_is_url_valid_fragments(self):
        valid_link = 'https://www.google.com/#about_us'
        truth_value = is_url_valid(valid_link)
        self.assertFalse(truth_value)

    def test_is_url_valid_failure(self):
        valid_link = 'https://www.google.com'
        truth_value = is_url_valid(valid_link)
        self.assertTrue(truth_value)


if __name__ == '__main__':
    unittest.main()
