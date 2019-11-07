# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


from celery import Celery
from tornado.httpclient import HTTPClient
app = Celery('tasks')
app.config_from_object('celeryconfig')
@app.task
def get_html(url):
    http_client = HTTPClient()
    try:
        response = http_client.fetch(url,follow_redirects=True)
        return response.body
    except http_client.HTTPError as e:
        return None
    http_client.close()