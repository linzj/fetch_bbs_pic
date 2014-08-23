import HttpFetchProcess, PageRoutines, ImageSaver
from Print import printDebug, printError
import urlparse, re


class HttpRequest(object):
    def __init__(self, host, path, body = None, jar = None):
        self.host = host
        self.path = path
        self.body = body
        self.jar = jar

    def __str__(self):
        return 'host: %s, path: %s, body: %s' % (self.host, self.path, self.body)

class PageDelegateBase(object):
    def __init__(self):
        self.callback_ = None
        pass
    
    def get_from_url(self, http_request, callback):
        self.callback_ = callback
        HttpFetchProcess.newDownloader(self).download(http_request)

    def fail_to_get(self, http_request, err):
        printDebug('PageDelegate::fail_to_get: http_request: %s, err: %s' % (str(http_request), err))
    
    def save(self, http_request, data):
        self.callback_(data)

    def construct_request(self, url, http_request):
        if url.startswith('/'):
            return HttpRequest(http_request.host, url, jar = http_request.jar)
        elif not re.match('^\w+:\/\/', url):
            return HttpRequest(http_request.host, http_request.path[0 : http_request.path.rindex('/') + 1] + url, jar = http_request.jar)
        elif not url.startswith('http://'):
            printDebug('PageDelegateBase::construct_request: url not starts with http://: %s' % url)
            return None
        else:
            host_end = url[7:].index('/') + 7
            return HttpRequest(url[7 : host_end], url[host_end:], jar = http_request.jar)

class MainPageDelegate(PageDelegateBase):
    def __init__(self):
        super(MainPageDelegate, self).__init__()

    def do_children(self, topic_urls, http_request):
        for topic_url in topic_urls:
            delegate = TopicPageDelegate()
            http_request_new = self.construct_request(topic_url, http_request)
            printDebug('MainPageDelegate::do_children: handling topic: %s, request: (%s)' % (topic_url, http_request_new))
            PageRoutines.do_topic_page(http_request_new, {'imgs' : 'div.topic-figure.cc>img', 'next_page' : '', 'url_attrib' : 'src'}, delegate)

    def do_next_pages(self, next_pages, http_request):
        for next_page in next_pages:
            printDebug('MainPageDelegate::next_page: %s' % next_page)

class TopicPageDelegate(PageDelegateBase):
    def __init__(self):
        super(TopicPageDelegate, self).__init__()
        
    def do_img(self, image_urls, http_request):
        for image_url in image_urls:
            image_saver = ImageSaver.ImageSaver('./')
            http_request_new = self.construct_request(image_url, http_request)
            printDebug('TopicPageDelegate::do_img: handling img %s, new request: (%s)' % (image_url, http_request_new))
            HttpFetchProcess.newDownloader(image_saver).download(http_request_new)

    def do_next_pages(self, next_pages, http_request):
        for next_page in next_pages:
            printDebug('TopicPageDelegate::next_page: %s' % next_page)


