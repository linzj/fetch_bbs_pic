import Page, PageDelegate, HttpFetchProcess
import cookielib, time, sys
from Print import printDebug
from ImageSaver import flush_log


class SleepForClass(object):

    def __init__(self):
        self.count_ = 0

    def check(self):
        if self.count_ >= 100:
            sleep_if_not_empty()

    def inc_count(self):
        self.count_ += 1

    def sleep_if_not_empty(self):
        if self.count_:
            flush_log()
            printDebug('finished one pass, sleeping...')
            time.sleep(80)
            printDebug('begining next pass')
            self.count_ = 0


def get_args_read():
    if len(sys.argv) != 2:
        printError("need to specify map file")
        sys.exit(1);
    with open(sys.argv[1], 'r') as f:
        content = f.read()

    return eval(content)


def main():
    configure = get_args_read()
    if not 'host' in configure:
        printError('There should be "host" field in your map')
        sys.exit(1)
    if not 'path' in configure:
        printError('There should be "path" field in your map')
        sys.exit(1)
    if 'max_parallel_pages' in configure:
        MAX_PARALLEL_PAGES = configure['max_parallel_pages']
    else:
        MAX_PARALLEL_PAGES = 1
    cj = cookielib.MozillaCookieJar()
    cj.load('./cookies.txt')
    HttpFetchProcess.start()
    main_dict = configure
    main_request = PageDelegate.HttpRequest(configure['host'], configure['path'], jar = cj)
    new_page_requests = []
    sleeper = SleepForClass()
    while True:
        for i in range(MAX_PARALLEL_PAGES):
            main_page_delegate = PageDelegate.PageDelegate()
            if not new_page_requests:
                if i == 0:
                    request = main_request
                    _dict = main_dict
                    sleeper.sleep_if_not_empty()
                    Page.do_page(request, _dict, main_page_delegate, new_page_requests)
                    sleeper.inc_count()
                break
            else:
                request, _dict = new_page_requests.pop(0)
                Page.do_page(request, _dict, main_page_delegate, new_page_requests)
                sleeper.inc_count()

        while HttpFetchProcess.next():
            pass
        printDebug('<!------------------------------ count = ' + str(sleeper.count_))
        sleeper.check()

if __name__ == '__main__':
    main()
    
    
