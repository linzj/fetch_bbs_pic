from pyquery import PyQuery as pq, PyQuery
from Print import printDebug, printError
import random

"""
inputs:
1. url
2. cookie file jar (netxxx)
3. selection strings for page
"""

def do_get_url(http_request, page_delegate, callback):
    printDebug('Page::do_get_url')
    return page_delegate.get_from_url(http_request, callback)


class ListQuerier(object):
    def __init__(self, data):
        self.d_ = pq(data)

    def get_list(self, selection_string, url_attrib):
        urls = []
        for topic in self.d_(selection_string):
            urls.append(topic.attrib[url_attrib])
        return urls
        

def parse_for(querier, selection_string, url_attrib):
    _l = querier.get_list(selection_string, url_attrib)
    random.shuffle(_l)
    return _l


def get_next_page(querier, selection_string):
    return querier.get_list(selection_string, 'href')

def do_page(http_request, main_dict, page_delegate, new_page_requests):
    def get_url_callback(got_data):
        querier = ListQuerier(got_data)
        if 'sub' in main_dict:
            sub_dict = main_dict['sub']
            if not isinstance(sub_dict, dict):
                raise Exception('sub field nees to be a dict')
            children = parse_for(querier, main_dict['target'], main_dict['url_attrib'])
            page_delegate.do_page(children, http_request, sub_dict, new_page_requests)
        else:
            children = parse_for(querier, main_dict['target'], main_dict['url_attrib'])
            page_delegate.do_resource(children, http_request)

        next_pages = get_next_page(querier, main_dict['next_page'])
        if next_pages:
            page_delegate.do_next_pages(next_pages[0], main_dict, http_request, new_page_requests)
        
    do_get_url(http_request, page_delegate, get_url_callback)

