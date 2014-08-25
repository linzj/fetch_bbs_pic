import multiprocessing, urllib2, traceback, gzip
from StringIO import StringIO
from Print import printDebug

pool = None
queue = []
delegator_map = {}
delegator_id = 0

def start():
    global pool
    if pool:
       return
    pool = multiprocessing.Pool(15)

def next():
    global queue, delegator_map
    if not queue:
        return False
    next_ = queue.pop(0)
    stub = next_.get()
    file_delegator, http_request = delegator_map[stub.file_delegator_id_]
    del delegator_map[stub.file_delegator_id_]
    if stub.is_save_:
        printDebug('HttpFetchProcess::next: stub.is_save_ = True, len(stub.data_) = %d' % (len(stub.data_)))
        file_delegator.save(http_request, stub.data_)
    else:
        printDebug('HttpFetchProcess::next: stub.is_save_ = False, stub.errstring_ = %s' % (stub.errstring_))
        file_delegator.fail_to_get(http_request, stub.errstring_)
    return True

def assign_delegator_(file_delegator):
    global delegator_id, delegator_map
    delegator_map[delegator_id] = [ file_delegator ]
    tmp = delegator_id
    delegator_id += 1
    return tmp

def newDownloader(file_delegator):
    return DownladerStub(assign_delegator_(file_delegator))

def worker(stub, url_request):
    printDebug('HttpFetchProcess::worker')
    HttpDownloader(stub).download(url_request)
    return stub
# copy from HttpDownloader.py
# make it adapted to multiprocessing
class HttpDownloader(object):
    def __init__(self, file_delegator):
        self.file_delegator_ = file_delegator

    def get_base_header_(self, url_request):
        ret_list = (('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
        ('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2'),
        ('User-Agent', 'User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'),
        ('Referer', 'http://' + url_request.get_host()),
        ('Accept-encoding', 'gzip'),
        )
        return ret_list


    def download(self, url_request):
        self.set_base_header_(url_request)
        try:
            f = urllib2.urlopen(url_request)
            if f.info().get('Content-Encoding') == 'gzip':
                buf = StringIO(f.read())
                f = gzip.GzipFile(fileobj=buf)
            return self.file_delegator_.save(f.read())
        except Exception as e:
            traceback.print_exc(e)
            self.file_delegator_.fail_to_get(str(e))

    def set_base_header_(self, url_request):
        for name, value in self.get_base_header_(url_request):
            url_request.add_header(name, value)

class FileDelegatorStub(object):
    def __init__(self, file_delegator_id):
        self.file_delegator_id_ = file_delegator_id
        self.is_save_ = False
        self.errstring_ = None
        self.url_request_ = None
        self.data_ = None

    def save(self, data):
        self.data_ = data
        self.is_save_ = True

    def fail_to_get(self, errstring):
        self.errstring_ = errstring

class DownladerStub(object):
    def __init__(self, file_delegator_id):
        self.file_delegator_id_ = file_delegator_id

    def download(self, http_request):
        global pool, queue, delegator_map
        file_delegator_stub = FileDelegatorStub(self.file_delegator_id_)
        delegator_map[self.file_delegator_id_].append(http_request)
        url_request = urllib2.Request('http://' + http_request.host + '/' + http_request.path)
        http_request.jar.add_cookie_header(url_request)
        queue.append(pool.apply_async(worker, (file_delegator_stub, url_request)))

