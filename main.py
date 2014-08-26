import PageRoutines, PageDelegate, HttpFetchProcess
import cookielib, time
from Print import printDebug

def main():
    main_page_delegate = PageDelegate.MainPageDelegate()
    cj = cookielib.MozillaCookieJar()
    cj.load('./cookies.txt')
    HttpFetchProcess.start()
    while True:
        PageRoutines.do_main_page(PageDelegate.HttpRequest('www.douban.com', '/group/', jar = cj), {'topic' : 'td.td-subject>a.title', 'next_page' : 'span.next>a', 'url_attrib' : 'href'}, main_page_delegate)
        while HttpFetchProcess.next():
            pass
        printDebug('finished one pass, sleeping...')
        time.sleep(120)
        printDebug('begining next pass')

if __name__ == '__main__':
    main()
    
    
