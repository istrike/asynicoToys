import tornado.web


class PageNotFound(tornado.web.RequestHandler):
    def get(self):
        self.set_status(404)
        self.render('404.html', page_title="NotFound")
