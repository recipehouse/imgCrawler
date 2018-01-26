#!/usr/bin/env python

from icrawler.builtin import GoogleImageCrawler

import sys

#keywords = ' '.join(sys.argv[1:])

filePath = str(sys.argv[1]).strip('[]')

with open(filePath, "r") as f:
    for line in f:
        google_crawler = GoogleImageCrawler(parser_threads=8, downloader_threads=8,storage={'root_dir': line})
        google_crawler.crawl(keyword = line, max_num=400, date_min=None, date_max=None, min_size=(400,400), max_size=None)

