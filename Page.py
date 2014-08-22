from pyquery import PyQuery as pq, PyQuery
from Print import printDebug, printError

"""
inputs:
1. url
2. cookie file jar (netxxx)
3. selection strings for page
"""

def do_get_url(http_request, jar, page_delegate):
    return page_delegate.get_from_url(http_request, jar)


class ListQuerier(object):
    def __init__(self, data):
        self.d_ = pq(data)

    def get_list(self, selection_string, url_attrib):
        urls = []
        for topic in self.d_(selection_string):
            urls.append(topic.attrib[url_attrib])
        return urls
        

def parse_for(querier, selection_string, url_attrib):
    return querier.get_list(selection_string, url_attrib)


def get_next_page(querier, selection_string):
    return querier.get_list(selection_string, 'href')

def do_page(http_request, jar, selection_strings, page_delegate, is_main_page):
    got_data = do_get_url(http_request, jar, page_delegate)
    querier = ListQuerier(got_data)
    if is_main_page:
        children = parse_for(querier, selection_strings['topic'], selection_strings['url_attrib'])
        page_delegate.do_children(children, jar)
    else:
        children = parse_for(querier, selection_strings['imgs'], selection_strings['url_attrib'])
        page_delegate.do_img(children, jar)

    next_pages = get_next_page(querier, selection_strings['next_page'])
    page_delegate.do_next_pages(next_pages)

