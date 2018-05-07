import tornado.web
from tornado import gen


class NavBarModule(tornado.web.UIModule):
    def render(self, navbar):
        return self.render("sdf")

    @gen.coroutine
    def get_navbar(self):
        client = self.settings["mongo"]
        client.find
