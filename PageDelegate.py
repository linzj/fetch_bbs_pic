import httplib, HttpDownloader
from Print import printDebug, printError


class HttpRequest(object):
    def __init__(self, method, host, path, body = None):
        self.method = method
        self.host = host
        self.path = path
        self.body = body

    def __str__(self):
        return 'method: %s, host: %s, path: %s, body: %s' % (self.method, self.host, self.path, self.body)

class PageDelegateBase(object):
    def __init__(self):
        pass
    
    def gen_head_from_jar(self, jar):
        _ret_dict_ = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2'
        }
    def get_from_url(self, http_request, jar):
        header = self.gen_head_from_jar(jar)
        hc = httplib.HTTPConnection(http_request.host)
        hc.request(http_request.method, http_request.path, header=header)
        response = hc.getresponse()
        if response.status != 200:
            printDebug('response.status = %d, returning None' % response.status)
            return None
        return response.read()
