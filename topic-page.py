from pyquery import PyQuery as pq, PyQuery

def do_topic_page(url, jar):
    data = do_fetch_topic(url, jar)
    if (isTopicUpdated(data, url))
        img_urls = do_query_topic(data)
        do_imgs(img_urls, jar)
