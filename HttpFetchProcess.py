import multiprocessing, urllib2, traceback, gzip
from StringIO import StringIO
from Print import printDebug
from Queue import Full


started = False
output_queue = multiprocessing.Queue()
arg_queue = multiprocessing.Queue()
requests_count = 0
delegator_map = {}
delegator_id = 0

def start():
    global started
    if started:
       return
    started = True
    for i in range(15):
        p = multiprocessing.Process(target = process_worker, args = (arg_queue, output_queue))
        p.start()

def next():
    global output_queue, delegator_map, requests_count
    if not requests_count:
        return False
    while True:
        try:
            stub = output_queue.get(block = True, timeout = 30)
            requests_count -= 1
            break
        except Full:
            printDebug('HttpFetchProcess::next: wait for 30 and nothing returns')
            continue

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

def process_worker(arg_queue, output_queue):
    while True:
        stub, url_request = arg_queue.get()

        output_queue.put(worker(stub, url_request))

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
            f = urllib2.urlopen(url_request, timeout = 10)
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
        global pool, delegator_map, requests_count
        file_delegator_stub = FileDelegatorStub(self.file_delegator_id_)
        delegator_map[self.file_delegator_id_].append(http_request)
        url_request = urllib2.Request('http://' + http_request.host + http_request.path)
        http_request.jar.add_cookie_header(url_request)

        arg_queue.put((file_delegator_stub, url_request))
        requests_count += 1

