from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        # 爬虫调度器
        self.urls = url_manager.UrlManager()
        # 网页下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 网页解析器
        self.parser = html_parser.HtmlParser()
        # 爬取内容输出
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_count = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_count)
                self.urls.add_new_urls(new_urls)

                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count = count + 1
            except:
                print("爬取失败")

        self.outputer.output_html()

if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)