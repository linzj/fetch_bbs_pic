from pyquery import PyQuery as pq, PyQuery

def do_imgs(topic_url, img_url, jar):
    if not topicTreeOwnUrl(topic_url, img_url):
        if downloadImg(topic_url, img_url, jar):
            updateTopicTree(topic_url, img_url)
