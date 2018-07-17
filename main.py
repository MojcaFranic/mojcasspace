__author__ = 'mojcafranic'

#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        self.render_template("index.html")

class PortfolioHandler(BaseHandler):
    def get(self):
        self.render_template("portfolio.html")

class CvHandler(BaseHandler):
    def get(self):
        self.render_template("cv.html")

class LivingRoomHandler(BaseHandler):
    def get(self):
        self.render_template("livingroom.html")

class BathroomHandler(BaseHandler):
    def get(self):
        self.render_template("bathroom.html")

class FursprayHandler(BaseHandler):
    def get(self):
        self.render_template("furspray.html")

class ArtshopHandler(BaseHandler):
    def get(self):
        self.render_template("artshop.html")

class BarHandler(BaseHandler):
    def get(self):
        self.render_template("bar.html")

class ZacasnoHandler(BaseHandler):
    def get(self):
        self.render_template("zacasno.html")

class HotelHandler(BaseHandler):
    def get(self):
        self.render_template("hotel.html")

class JajceHandler(BaseHandler):
    def get(self):
        self.render_template("jajce.html")

class HomeHandler(BaseHandler):
    def get(self):
        self.render_template("home.html")

class DiplomaHandler(BaseHandler):
    def get(self):
        self.render_template("diploma.html")

class LilyHandler(BaseHandler):
    def get(self):
        self.render_template("lily.html")

class QubikHandler(BaseHandler):
    def get(self):
        self.render_template("qubik.html")

class ClubtableHandler(BaseHandler):
    def get(self):
        self.render_template("clubtable.html")

class NightstandHandler(BaseHandler):
    def get(self):
        self.render_template("nightstand.html")

class GraphicHandler(BaseHandler):
    def get(self):
        self.render_template("graphic.html")

class WebHandler(BaseHandler):
    def get(self):
        self.render_template("web.html")

class OtherHandler(BaseHandler):
    def get(self):
        self.render_template("other.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/portfolio', PortfolioHandler),
    webapp2.Route('/cv', CvHandler),
    webapp2.Route('/livingroom', LivingRoomHandler),
    webapp2.Route('/bathroom', BathroomHandler),
    webapp2.Route('/furspray', FursprayHandler),
    webapp2.Route('/artshop', ArtshopHandler),
    webapp2.Route('/bar', BarHandler),
    webapp2.Route('/zacasno', ZacasnoHandler),
    webapp2.Route('/hotel', HotelHandler),
    webapp2.Route('/jajce', JajceHandler),
    webapp2.Route('/home', HomeHandler),
    webapp2.Route('/diploma', DiplomaHandler),
    webapp2.Route('/lily', LilyHandler),
    webapp2.Route('/qubik', QubikHandler),
    webapp2.Route('/clubtable', ClubtableHandler),
    webapp2.Route('/nightstand', NightstandHandler),
    webapp2.Route('/graphic', GraphicHandler),
    webapp2.Route('/web', WebHandler),
    webapp2.Route('/other', OtherHandler),


], debug=True)