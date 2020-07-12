import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if response.status != 200:
            return None
        print(response.status)
        return response.read()