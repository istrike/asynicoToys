import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.escape
from tornado.options import define, options
from config import settings
from handlers import IndexHandler
from handlers import PageNotFound
import motor

# 定义一个默认的端口


define("port", default=8000, help="run port ", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        client = motor.motor_tornado.MotorClient('mongodb://localhost:27017')["mydb"]
        settings["mongo"]=client
        handler_list = [
            (r"/", IndexHandler.IndexHandler),
            (r'.*', PageNotFound.PageNotFound),
        ]
        tornado.web.Application.__init__(self, handler_list, **settings)


if __name__ == "__main__":
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print('start server...')
    tornado.ioloop.IOLoop.instance().start()
