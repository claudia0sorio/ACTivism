
import webapp2
import os
import jinja2
from google.appengine.ext import ndb




jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class CalendarHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_current_dir.get_template('blank.html')
        self.response.write(template.render())




#class HomePageHandler(webapp2.RequestHandler):
#    def get(self):




app = webapp2.WSGIApplication([
    ('/calendar', CalendarHandler),
], debug=True)




# app = webapp2.WSGIApplication([
    # ('/calendar', CalendarHandler),
    # ('/', HomePageHandler),
# ], debug=True)




#    template= jinja_current_dir.get_template('my_blog.html')
#    self.response.write(template.render())
#    template_vars={'title': title, 'main': main, 'username':username}
#    template=jinja_current_dir.get_template('posts.html')
#    self.response.write(template.render(template_vars))
