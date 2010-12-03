#!/usr/bin/env python
import os
import os.path
import re
import tornado.web
import tornado.wsgi
import unicodedata
import wsgiref.handlers

from google.appengine.api import users


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world!")

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "xsrf_cookies": True,
    "debug": os.environ.get("SERVER_SOFTWARE", "").startswith("Development/"),
}

application = tornado.wsgi.WSGIApplication([
    (r"/", HomeHandler),
], **settings)


def main():
    wsgiref.handlers.CGIHandler().run(application)


if __name__ == "__main__":
    main()


# import wsgiref.handlers
# from google.appengine.ext import webapp
# 
# 
# class Hello(webapp.RequestHandler):
#     def get(self):
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.out.write('Hello world!')
# 
# def application():
#     return webapp.WSGIApplication([('/', Hello)], debug=True)
# 
# def main():
#     wsgiref.handlers.CGIHandler().run(application())
# 
# if __name__ == '__main__':
#     main()