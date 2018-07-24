
import webapp2
import os
import jinja2
from google.appengine.ext import ndb



jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_current_dir.get_template('templates/calendar.html')

        self.response.write(template.render())
class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_current_dir.get_template('templates/home.html')
        self.response.write(template.render())
class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_current_dir.get_template('templates/about_us.html')
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    ('/calendar', MainHandler),
    ('/', HomePageHandler),
    ('/about_us', AboutUsHandler),
], debug=True)
