# -*- coding: utf-8 -*-
import scrapy


class BlogSpiderSpider(scrapy.Spider):
    name = 'blog_spider'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/']

    def parse(self, response):
        print("网页信息：")
        print(response.url)
