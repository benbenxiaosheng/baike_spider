
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  #待爬取的url,在管理器内
        self.old_urls = set()  #已爬取的url

    # 向管理器里添加一个url
    def add_new_url(self, url):
        if url is None :
            return
        if url not in self.new_urls and url not in self.old_urls :
            self.new_urls.add(url)

    # 向管理器里添加批量url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            if url in self.new_urls or url in self.old_urls :
                return
        for url in urls:
            self.new_urls.add(url)

    # 判断添加的url是否重复
    def has_new_url(self):
        # 如果新的url长度不等于0，就说明有的待爬取的url
        return len('self.new_urls') != 0

    # 从url管理器内获取一个新的url 去爬取
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

