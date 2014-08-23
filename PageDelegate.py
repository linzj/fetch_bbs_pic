import HttpDownloader
from Print import printDebug, printError


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
