from pyquery import PyQuery as pq, PyQuery
from Print import printDebug, printError
import random

"""
inputs:
1. url
2. cookie file jar (netxxx)
3. selection strings for page
"""

class PageLimit(object):
    def __init__(self, limit):
        self.limit_ = limit

    def dec(self):
        self.limit_ -= 1

    def is_out(self):
        return self.limit_  <= 0

class PageRequest(object):
    def __init__(self, http_request, _dict):
        self.http_request_ = http_request
        self.dict_ = _dict
        self.limit_ = None

    def get_reqeust(self):
        return self.http_request_

    def get_dict(self):
        return self.dict_

    def get_limit(self):
        return self.limit_

    def clone_with(self, new_http_request, _dict = None):
        if not _dict:
            _dict = self.dict_
        new_clone = PageRequest(new_http_request, _dict)
        new_clone.limit_ = self.limit_
        return new_clone

    def set_limit(self, limit):
        self.limit_ = limit

def do_get_url(http_request, page_delegate, callback):
    printDebug('Page::do_get_url')
    return page_delegate.get_from_url(http_request, callback)


class ListQuerier(object):
    def __init__(self, data):
        self.d_ = pq(data)

    def get_list(self, selection_string, url_attribs):
        urls = []
        for topic in self.d_(selection_string):
            if isinstance(url_attribs, list):
                for url_attrib in url_attribs:
                    try:
                        urls.append(topic.attrib[url_attrib])
                        break
                    except:
                        continue
            else:
                try:
                    urls.append(topic.attrib[url_attribs])
                except:
                    pass

        return urls
        

def parse_for(querier, selection_string, url_attrib):
    _l = querier.get_list(selection_string, url_attrib)
    random.shuffle(_l)
    return _l


def get_next_page(querier, selection_string):
    return querier.get_list(selection_string, 'href')

def do_page(page_request, page_delegate, new_page_requests):
    def get_url_callback(got_data):
        querier = ListQuerier(got_data)
        main_dict = page_request.get_dict()
        if 'sub' in main_dict:
            sub_dict = main_dict['sub']
            if not isinstance(sub_dict, dict):
                raise Exception('sub field nees to be a dict')
            children = parse_for(querier, main_dict['target'], main_dict['url_attrib'])
            if 'randomize' in main_dict:
                children = page_delegate.do_randomize(children, main_dict)
            page_delegate.do_page(children, page_request, sub_dict, new_page_requests)
        else:
            children = parse_for(querier, main_dict['target'], main_dict['url_attrib'])
            page_delegate.do_resource(children, page_request.get_reqeust())

        next_pages = get_next_page(querier, main_dict['next_page'])
        if next_pages:
            page_delegate.do_next_pages(next_pages[0], page_request, new_page_requests)
        
    do_get_url(page_request.get_reqeust(), page_delegate, get_url_callback)

