import scrapy


class WinstonSpider3(scrapy.Spider):

    name = 'runArg'

    def start_requests(self):
        url = 'http://lab.scrapyd.cn/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        winston = response.css('div.quote')
        for v in winston:
            text = v.css('.text::text').extract_first()
            tags = v.css('.tags .tag::text').extract()
            # 数组转换为字符串
            tags = ','.join(tags)
            fileName = '%s-语录.txt' % tags
            with open(fileName, 'a+', encoding='utf-8') as f:
                f.write(text)
                f.write('\n')
                f.write('标签：' + tags)
                f.write('\n')
                f.close()

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
