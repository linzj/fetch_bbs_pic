import httplib
from Print import printDebug, printError


class HttpRequest(object):
    def __init__(self, method, host, path):
        self.method = method
        self.host = host
        self.path = path

class MainPageDelegateBase(object):
    def __init__(self):
        pass

    def get_from_url(self, http_request, jar):
        hc = httplib.HTTPConnection(http_request.host)
        header = self.gen_head_from_jar(jar)
        hc.request(http_request.method, http_request.path, header=header)
        response = hc.getresponse()
        if response.status != 200:
            printDebug('response.status = %d, returning None' % response.status)
            return None
        return response.read()
