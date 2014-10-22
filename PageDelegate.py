import HttpFetchProcess,  ImageSaver
from Print import printDebug, printError
import urlparse, re, os.path


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
        self.http_request_ = None
        pass
    
    def get_from_url(self, http_request, callback):
        self.callback_ = callback
        self.http_request_ = http_request
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

class PageDelegate(PageDelegateBase):
    def __init__(self):
        super(PageDelegate, self).__init__()

    def do_page(self, topic_urls, http_request, sub_dict, new_page_requests):
        for topic_url in topic_urls:
            http_request_new = self.construct_request(topic_url, http_request)
            new_page_requests.append((http_request_new, sub_dict))

    def do_resource(self, resource_urls, http_request):
        for resource_url in resource_urls:
            path = resource_url
            file_name =  path[path.rindex('/') + 1:]
            if os.path.isfile(file_name):
                continue
            image_saver = ImageSaver.ImageSaver('./', self.http_request_)
            http_request_new = self.construct_request(resource_url, http_request)
            printDebug('PageDelegate::do_img: handling img %s, new request: (%s)' % (resource_url, http_request_new))
            HttpFetchProcess.newDownloader(image_saver).download(http_request_new)

    def do_next_pages(self, next_page, main_dict, http_request, new_page_requests):
        new_page_requests.append((self.construct_request(next_page, http_request), main_dict))

