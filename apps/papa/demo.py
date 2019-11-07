# -*- coding=utf-8 -*-
#!/usr/bin/env python
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'



import time
from datetime import timedelta

try:
    from HTMLParser import HTMLParser
    from urlparse import urljoin, urldefrag
except ImportError:
    from html.parser import HTMLParser
    from urllib.parse import urljoin, urldefrag

from tornado import httpclient, gen, ioloop, queues

 # 设置要爬取的网址
base_url = 'http://www.11face.com'
 # 设置worker数量
concurrency = 10
 # 此代码会获取base_url下的所有其他url
@gen.coroutine
def get_links_from_url(url):

    try:
        # 通过异步向url发起请求
        response = yield httpclient.AsyncHTTPClient().fetch(url)
        print('fetched %s' % url)
        # 响应如果是字节类型 进行解码
        html = response.body if isinstance(response.body, str) \
            else response.body.decode(errors='ignore')
        # 构建url列表
        urls = [urljoin(url, remove_fragment(new_url))
                for new_url in get_links(html)]
    except Exception as e:
        print('Exception: %s %s' % (e, url))
        # 报错返回空列表
        raise gen.Return([])
    # 返回url列表
    raise gen.Return(urls)


def remove_fragment(url):
    #去除锚点
    pure_url, frag = urldefrag(url)

    return pure_url


def get_links(html):
    #从html页面里提取url
    class URLSeeker(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.urls = []

        def handle_starttag(self, tag, attrs):
            href = dict(attrs).get('href')
            if href and tag == 'a':
                self.urls.append(href)

    url_seeker = URLSeeker()
    url_seeker.feed(html)
    return url_seeker.urls


@gen.coroutine
def main():
    # 创建队列
    q = queues.Queue()
    # 记录开始时间戳
    start = time.time()
    # 构建两个集合
    fetching, fetched = set(), set()

    @gen.coroutine
    def fetch_url():
        # 从队列中取出数据
        current_url = yield q.get()
        try:
            # 如果取出的数据在队列中已经存在  返回
            if current_url in fetching:
                return

            print('fetching %s' % current_url)
            # 如果不存在添加到集合当中
            fetching.add(current_url)
            # 从新放入的链接中继续获取链接
            urls = yield get_links_from_url(current_url)
            # 将已经请求玩的url放入第二个集合
            fetched.add(current_url)

            for new_url in urls:
                # Only follow links beneath the base URL
                # 如果链接是以传入的url开始则放入队列
                if new_url.startswith(base_url):
                    yield q.put(new_url)

        finally:
            # 队列内数据减一
            q.task_done()

    @gen.coroutine
    def worker():
        while True:
            # 保证程序持续运行
            yield fetch_url()
    # 将第一个url放入队列
    q.put(base_url)

    # Start workers, then wait for the work queue to be empty.
    for _ in range(concurrency):
        # 启动对应数量的worker
        worker()
    # 等待队列数据处理完成
    yield q.join(timeout=timedelta(seconds=300))
    # 如果两个集合不相等抛出异常
    assert fetching == fetched
    # 打印执行时间
    print('Done in %d seconds, fetched %s URLs.' % (
        time.time() - start, len(fetched)))


if __name__ == '__main__':
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)