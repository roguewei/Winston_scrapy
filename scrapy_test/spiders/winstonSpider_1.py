import scrapy


class WinstonSpider1(scrapy.Spider):
    name = 'runName'

    start_urls = [  # 另外一种写法，无需定义start_requests方法
        'http://lab.scrapyd.cn/page/1/',
        # 'http://lab.scrapyd.cn/page/2/',
    ]

    def parse(self, response):
        mingyan = response.css('div.quote')

        for v in mingyan:
            # 提取名言
            text = v.css('.text::text').extract_first()
            # 提取作者
            autor = v.css('.author::text').extract_first()
            # 提取标签
            tags = v.css('.tags .tag::text').extract()
            # 数组转换为字符串
            tags = ','.join(tags)

            fileName = '%s-语录.txt' % autor  # 爬取的内容存入文件，文件名为：作者-语录.txt
            with open(fileName, 'a+') as f:
                f = open(fileName, "a+")  # 追加写入文件
                f.write(text)  # 写入名言内容
                f.write('\n')  # 换行
                f.write('标签：' + tags)  # 写入标签
                f.write('\n')  # 换行
                f.close()  # 关闭文件操作
