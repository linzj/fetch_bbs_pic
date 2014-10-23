import Page, PageDelegate, HttpFetchProcess
import cookielib, time
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

MAX_PARALLEL_PAGES=10


def main():
    cj = cookielib.MozillaCookieJar()
    cj.load('./cookies.txt')
    HttpFetchProcess.start()
    #main_dict = {
    #    'target' : 'td.td-subject>a.title',
    #    'next_page' : 'span.next>a',
    #    'url_attrib' : 'href',
    #    'sub' : {
    #        'target' : 'div.topic-figure.cc>img',
    #        'next_page' : '',
    #        'url_attrib' : 'src'},
    #}
    main_dict = {
        'target' : 'div.row>div.text>p>img',
        'next_page' : 'a.previous-comment-page',
        'url_attrib' : ['org_src', 'src'],
    }
    main_request = PageDelegate.HttpRequest('jandan.net', '/ooxx/', jar = cj)
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
                break
            else:
                request, _dict = new_page_requests.pop(0)
                Page.do_page(request, _dict, main_page_delegate, new_page_requests)

        while HttpFetchProcess.next():
            pass
        sleeper.inc_count()
        printDebug('<!------------------------------ count = ' + str(sleeper.count_))
        sleeper.check()

if __name__ == '__main__':
    main()
    
    
