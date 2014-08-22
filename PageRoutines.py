import Page

def do_main_page(http_request, jar, selection_strings, main_page_delegate):
    Page.do_page(http_request, jar, selection_strings, main_page_delegate, True)

def do_topic_page(http_request, jar, selection_strings, main_page_delegate):
    Page.do_page(http_request, jar, selection_strings, main_page_delegate, False)
