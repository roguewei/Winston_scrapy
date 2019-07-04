import scrapy


class WinstonSpider(scrapy.Spider):
    # 运行scrapy命令时的标识
    # 命令行执行：scrapy crawl runScrapyName
    name = "runScrapyName"

    # 方法一
    # 实现scrapy.Spider里的方法，由此方法通过下面链接爬取页面
    # def start_requests(self):
    #     # 定义爬取的链接
    #     urls = [
    #         'http://lab.scrapyd.cn/page/1/',
    #         'http://lab.scrapyd.cn/page/2/'
    #     ]
    #     for url in urls:
    #         # 将爬取到的数据交给parse方法去处理
    #         yield scrapy.Request(url=url, callback=self.myparse)

    # 方法一，这里的方法名可以自己定义
    # def myparse(self, response):
    #     """
    #     start_requests已经爬取到页面，那如何提取我们想要的内容呢？那就可以在这个方法里面定义。
    #     这里的话，并木有定义，只是简单的把页面做了一个保存，并没有涉及提取我们想要的数据，后面会慢慢说到
    #     也就是用xpath、正则、或是css进行相应提取，这个例子就是让你看看scrapy运行的流程：
    #     1、定义链接；
    #     2、通过链接爬取（下载）页面；
    #     3、定义规则，然后提取数据；
    #     """
    #     # 根据上面的链接提取分页,如：/page/1/，提取到的就是：1
    #     page = response.url.split('/')[-2]
    #     print(page+"-----------")
    #     # 拼接文件名，如果是第一页，最终文件名便是：winston-1.html
    #     filename = 'winston-%s.html' % page
    #     # python文件操作
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('save file: %s' % filename)

    # 方法二
    start_urls = [
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/'
    ]

    # 方法二，这里的方法名必须使用parse，方法内部实现跟方法一一样
    def parse(self, response):
        """
        start_requests已经爬取到页面，那如何提取我们想要的内容呢？那就可以在这个方法里面定义。
        这里的话，并木有定义，只是简单的把页面做了一个保存，并没有涉及提取我们想要的数据，后面会慢慢说到
        也就是用xpath、正则、或是css进行相应提取，这个例子就是让你看看scrapy运行的流程：
        1、定义链接；
        2、通过链接爬取（下载）页面；
        3、定义规则，然后提取数据；
        """
        # 根据上面的链接提取分页,如：/page/1/，提取到的就是：1
        page = response.url.split('/')[-2]
        print(page+"-----------")
        # 拼接文件名，如果是第一页，最终文件名便是：winston-1.html
        filename = 'winston-%s.html' % page
        # python文件操作
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('save file: %s' % filename)
