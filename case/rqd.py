# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'

import tornado.ioloop
import tornado.web
import tornado.autoreload


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("python jwt hot load!!!")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/index", MainHandler),
        (r"/x", MainHandler),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    port = 3001
    print('start listen %d' % port)
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()