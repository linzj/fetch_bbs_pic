import HttpDownloader
from Print import printDebug, printError
import PageRoutines


class HttpRequest(object):
    def __init__(self, method, host, path, body = None, jar = None):
        self.method = method
        self.host = host
        self.path = path
        self.body = body
        self.jar = jar

    def __str__(self):
        return 'method: %s, host: %s, path: %s, body: %s' % (self.method, self.host, self.path, self.body)

class PageDelegateBase(object):
    def __init__(self):
        self.callback_ = None
        pass
    
    def get_base_header(self):
        _ret_dict_ = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2'
        }
        return _ret_dict_

    def get_from_url(self, http_request, callback):
        self.callback_ = callback
        HttpDownloader(self).download(http_request)

    def fail_to_get(self, http_request, err):
        printDebug('PageDelegate::fail_to_get: http_request: %s, err: %s' % (str(http_request), err))
    
    def save(self, http_request, data):
        self.callback_(data)

def MainPageDelegate(PageDelegateBase):
    def __init__(self):
        super(MainPageDelegate, self).__init__()

    def do_children(self, topic_urls, http_request):
        for topic_url in topic_urls:
            delegate = TopicPageDelegate()
            PageRoutines.do_topic_page(HttpRequest('GET', 'douban.com', '/'), {'imgs' : 'div.topic-figure.cc>img', 'next_page' : '', 'url_attrib' : 'src'}, delegate)

    def do_next_pages(self, next_pages, http_request):
        for next_page in next_pages:
            printTest('next_page: %s' % next_page)
