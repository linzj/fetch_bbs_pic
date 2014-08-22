import httplib


class HttpDownloader(object):
    def __init__(file_delegator):
        self.file_delegator_ = file_delegator

    def download(self, http_request, header, body, method):
        
        hc = httplib.HTTPConnection(http_request.host)
        header = self.gen_head_from_jar(jar)
        hc.request(http_request.method, http_request.path, body, header)
        response = hc.getresponse()
        if response.status != 200:
            printDebug('response.status = %d, returning None' % response.status)
            file_delegator_.fail_to_get(http_request)
            return
        return file_delegator_.save(http_request, response.read())

