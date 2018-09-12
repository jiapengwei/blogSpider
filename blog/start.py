# -*- coding: utf-8 -*-

from scrapy import cmdline


'''

scrapy crawl blog_spider
scrapy crawl blog_spider -o test.json
scrapy crawl blog_spider -o test.csv
'''



cmdline.execute("scrapy crawl blog_spider".split())