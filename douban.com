{
    'target' : 'td.td-subject>a.title',
    'next_page' : 'span.next>a',
    'page_limit' : 150,
    'url_attrib' : 'href',
    'sub' : {
        'target' : 'div.topic-figure.cc>img',
        'next_page' : '',
        'url_attrib' : 'src'},
    'host' : 'www.douban.com',
    'path' : '/group/',
    'max_parallel_pages' : 10,
}

