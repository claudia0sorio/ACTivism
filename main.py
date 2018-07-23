
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
        template= jinja_current_dir.get_template('templates/calendar.html')
=======
        template= jinja_current_dir.get_template('/templates/calendar.html')
>>>>>>> 7dd0b567ce9a11b042825244512bd0b2952d1ed0
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
