import Page, PageDelegate, HttpFetchProcess
import cookielib, time, sys, random
from Print import printDebug
from ImageSaver import flush_log


class SleepForClass(object):

    def __init__(self):
        self.count_ = 0

    def check(self):
        if self.count_ >= 100:
            self.sleep_if_not_empty()

    def inc_count(self):
        self.count_ += 1

    def sleep_if_not_empty(self):
        if self.count_:
            flush_log()
            sleepTime = random.uniform(80, 100)
            printDebug('finished one pass, sleeping for %f...' % sleepTime)
            time.sleep(sleepTime)
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
    if 'page_limit' in configure:
        page_limit_count = configure['page_limit']
    else:
        page_limit_count = 0
    cj = cookielib.MozillaCookieJar()
    cj.load('./cookies.txt')
    HttpFetchProcess.start()
    main_dict = configure
    main_request = PageDelegate.HttpRequest(configure['host'], configure['path'], jar = cj)
    main_page_request = Page.PageRequest(main_request, main_dict)
    new_page_requests = []
    sleeper = SleepForClass()
    while True:
        for i in range(MAX_PARALLEL_PAGES):
            main_page_delegate = PageDelegate.PageDelegate()
            if not new_page_requests:
                if i == 0:
                    page_request = main_page_request
                    if page_limit_count != 0:
                        page_request.set_limit(Page.PageLimit(page_limit_count))
                    sleeper.sleep_if_not_empty()
                    Page.do_page(page_request, main_page_delegate, new_page_requests)
                    sleeper.inc_count()
                break
            else:
                page_request = new_page_requests.pop(0)
                page_limit = page_request.get_limit()
                if page_limit:
                    if page_limit.is_out():
                        new_page_requests = []
                        break
                    page_limit.dec()
                Page.do_page(page_request, main_page_delegate, new_page_requests)
                sleeper.inc_count()

        while HttpFetchProcess.next():
            pass
        printDebug('<!------------------------------ count = ' + str(sleeper.count_))
        sleeper.check()

if __name__ == '__main__':
    main()
    
    
