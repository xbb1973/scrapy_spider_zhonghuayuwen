# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
class ZhonghuayuwenPipeline(object):

    fieldnames = ['char_item', 'char2text_list_len', 'char2text_list']

    def open_spider(self, spider):
        # self.file = open('zhonghuayuwen.json', 'w', encoding='utf-8')
        with open('zhonghuayuwen.csv', 'w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
        pass

    def process_item(self, item, spider):
        # content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        # print(content)
        # print('---content---')
        # self.file.write(content)

        with open('zhonghuayuwen.csv', 'a', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow(dict(item))

        return item

    def close_spider(self, spider):
        # self.file.close()
        pass
