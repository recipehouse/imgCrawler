#!/usr/bin/env python

from icrawler.builtin import GoogleImageCrawler

import sys

keywords = ' '.join(sys.argv[1:])

google_crawler = GoogleImageCrawler(parser_threads=8, downloader_threads=8,
                                    storage={'root_dir': keywords})
google_crawler.crawl(keyword = keywords, max_num=1000,
                     min_size=(500,500), max_size=None)

