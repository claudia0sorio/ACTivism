
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








app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/aboutme', AboutMeHandler),
    ('/posts', PostsHandler),
], debug=True)



#    template= jinja_current_dir.get_template('my_blog.html')
#    self.response.write(template.render())
#    template_vars={'title': title, 'main': main, 'username':username}
#    template=jinja_current_dir.get_template('posts.html')
#    self.response.write(template.render(template_vars))
