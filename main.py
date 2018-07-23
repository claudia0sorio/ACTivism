
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
<<<<<<< HEAD
        template= jinja_current_dir.get_template('/templates/calendar.html')
=======

        template= jinja_current_dir.get_template('templates/calendar.html')

        template= jinja_current_dir.get_template('/templates/calendar.html')

>>>>>>> 1f5bece821d2cd8923f87fb6cc5b3588f210843d
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
