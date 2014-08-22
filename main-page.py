from pyquery import PyQuery as pq, PyQuery
import httplib
from Print import printDebug, printError

"""
inputs:
1. url
2. cookie file jar (netxxx)
3. selection string for main-page
"""

def gen_head_from_jar(jar):
    main_page_delegate.gen_head_from_jar(jar)

def do_get_url(http_request, jar):
    hc = httplib.HTTPConnection(http_request.host)
    header = gen_head_from_jar(jar)
    hc.request(http_request.method, http_request.path, header=header)
    response = hc.getresponse()
    if response.status != 200
        printDebug('response.status = %d, returning None' % response.status)
        return None
    return response.read()

class ListQuerier(object):
    def __init__(self, data):
        self.d_ = pq(data)

    def get_list(self, selection_string):
        urls = []
        for topic in d(selection_string):
            urls.append(topic.href)
        return urls
        

def parse_for_topic(querier, selection_string):
    return querier.get_list(selection_string)

def do_children(children, jar, main_page_delegate):
    main_page_delegate.do_children(children, jar)

def get_next_page(querier, selection_string):
    return querier.get_list(selection_string)

def do_main_page(http_request, jar, selection_strings, main_page_delegate):
    printDebug('do_main_page: %s' % (str(http_request)))

    got_data = do_get_url(http_request, jar)
    querier = ListQuerier(got_data)
    children = parse_for_topic(querier, selection_strings.topic)
    do_children(children, jar, main_page_delegate)
    next_pages = get_next_page(querier, selection_strings.next_page)
    main_page_delegate.do_next_pages(next_pages)

