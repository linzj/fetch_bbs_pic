import Page, PageDelegate, HttpFetchProcess
import cookielib, time
from Print import printDebug
from ImageSaver import flush_log

def main():
    main_page_delegate = PageDelegate.PageDelegate()
    cj = cookielib.MozillaCookieJar()
    cj.load('./cookies.txt')
    HttpFetchProcess.start()
    main_dict = {
        'target' : 'td.td-subject>a.title',
        'next_page' : 'span.next>a',
        'url_attrib' : 'href',
        'sub' : {
            'target' : 'div.topic-figure.cc>img',
            'next_page' : '',
            'url_attrib' : 'src'},
    }
    main_request = PageDelegate.HttpRequest('www.douban.com', '/group/', jar = cj)
    new_page_requests = []
    count = 0
    while True:
        if not new_page_requests:
            request = main_request
            _dict = main_dict
        else:
            request, _dict = new_page_requests.pop(0)

        Page.do_page(request, _dict, main_page_delegate, new_page_requests)
        while HttpFetchProcess.next():
            pass
        count += 1
        printDebug('<!------------------------------ count = ' + str(count))
        if count >= 100:
            flush_log()
            printDebug('finished one pass, sleeping...')
            time.sleep(80)
            printDebug('begining next pass')
            count = 0

if __name__ == '__main__':
    main()
    
    
