import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.escape
from tornado.options import define, options
from config import settings
from handlers import IndexHandler

# 定义一个默认的端口
define("port", default=8000, help="run port ", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/", IndexHandler.IndexHandler), ]
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print('start server...')
    tornado.ioloop.IOLoop.instance().start()
