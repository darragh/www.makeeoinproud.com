import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
webapp.template.register_template_library('filters')
class IndexPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {}))


class MemorialPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        path = os.path.join(os.path.dirname(__file__), 'memorial.html')
        self.response.out.write(template.render(path, {}))

class MiniBookPage(webapp.RequestHandler):
    def get(self, page):
        if(page == None):
            self.redirect("/mini-book/1..2")
        else:
            self.response.headers['Content-Type'] = 'text/html'
            path = os.path.join(os.path.dirname(__file__), 'mini-book.html')
            def odd(x): return x % 2 == 1
            odd_pages = filter(odd, range(1,48))
            self.response.out.write(template.render(path, {"current_page" : int(page), "all_pages" : odd_pages}))


application = webapp.WSGIApplication([('/', IndexPage), ('/memorial', MemorialPage), (r'/mini-book(?:/|(?:/(\d\d?)\.\.\d\d?))?', MiniBookPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()