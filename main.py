from crawler import Crawler
import argparse


parser = argparse.ArgumentParser(description='Simple Web Crawler')
parser.add_argument('-u', '--url', metavar='', default='https://mix.com',
                    type=str, help='Seed URL for crawling')
parser.add_argument('-d', '--depth', metavar='', default=10,
                    type=int, help='Number of links to crawl over')
args = parser.parse_args()


if __name__ == '__main__':
    Crawler(args.url, args.depth)
