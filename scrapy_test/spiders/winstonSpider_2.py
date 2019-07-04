import scrapy


class WinstonSpider2(scrapy.Spider):

    name = 'runNext'

    start_urls = [
        'http://lab.scrapyd.cn/'
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
                f = open(fileName, "a+", encoding='utf-8')  # 追加写入文件
                f.write(text)  # 写入名言内容
                f.write('\n')  # 换行
                f.write('标签：' + tags)  # 写入标签
                f.write('\n')  # 换行
                f.close()  # 关闭文件操作

        # 接下来我们需要判断下一页是否存在，如果存在
        # 我们需要继续提交给parse执行关键看 scrapy 如何实现链接提交

        # css选择器提取下一页链接
        next_page = response.css('li.next a::attr(href)').extract_first()

        if next_page is not None:
            """
             如果是相对路径，如：/page/1
             urljoin能替我们转换为绝对路径，也就是加上我们的域名
             最终next_page为：http://lab.scrapyd.cn/page/2/
            """
            next_page = response.urljoin(next_page)
            print(next_page + '---------------------next_page')
            yield scrapy.Request(next_page, callback=self.parse)

