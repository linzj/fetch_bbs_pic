import urllib2


class HttpDownloader(object):
    def __init__(file_delegator):
        self.file_delegator_ = file_delegator

    def download(self, http_request):
        if http_request.jar:
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(http_request.jar))
        else:
            opener = urllib2.build_opener()
        self.set_base_header(opener)
        try:
            f = opener.open()
            return file_delegator_.save(http_request, f.read())
        except e:
            file_delegator_.fail_to_get(http_request, str(e))

    def set_base_header(self, opener):
        opener.addheaders(self.file_delegator_.get_base_header())

