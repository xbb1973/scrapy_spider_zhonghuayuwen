# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhonghuayuwenItem(scrapy.Item):
    # define the fields for your item here like:
    char_item = scrapy.Field()  # 3755个单字
    char2text_list_len = scrapy.Field()  # 由单字检索出来的文本行个数
    char2text_list = scrapy.Field()  # 由单字检索出来的文本行
