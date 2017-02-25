import urllib2, traceback

class HttpDownloader(object):
    def __init__(self, file_delegator):
        self.file_delegator_ = file_delegator

    def get_base_header_(self, http_request):
        ret_list = (('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
        ('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2'),
        ('User-Agent', 'User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'),
        ('Referer', 'http://' + http_request.host),
        )
        return ret_list


    def download(self, http_request):
        if http_request.jar:
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(http_request.jar))
        else:
            opener = urllib2.build_opener()
        self.set_base_header_(opener, http_request)
        try:
            host = http_request.host 
            ip = dnsResolver.resolve(http_request.host)
            if ip:
                host = ip
                printDebug('resovled host: ' + http_request.host + ';ip: ' + ip)
            else:
                printDebug('fails to resovled host: ' + http_request.host + ';ip: ' + ip)

            f = opener.open('http://' + host + '/' + http_request.path)
            return self.file_delegator_.save(http_request, f.read())
        except Exception as e:
            traceback.print_exc(e)
            self.file_delegator_.fail_to_get(http_request, str(e))

    def set_base_header_(self, opener, http_request):
        opener.addheaders = self.get_base_header_(http_request)

