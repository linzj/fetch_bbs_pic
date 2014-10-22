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
    while True:
        Page.do_page(PageDelegate.HttpRequest('www.douban.com', '/group/', jar = cj), main_dict, main_page_delegate)
        while HttpFetchProcess.next():
            pass
        flush_log()
        printDebug('finished one pass, sleeping...')
        time.sleep(80)
        printDebug('begining next pass')

if __name__ == '__main__':
    main()
    
    
