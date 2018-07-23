
import webapp2
import os
import jinja2
from google.appengine.ext import ndb

from django import template

from calendar import Calendar
import datetime

import re

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


register = template.Library()

@register.tag(name="get_calendar")
def do_calendar(parser, token):
    syntax_help = "syntax should be \"get_calendar for <month> <year> as <var_name>\""
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments, %s" % (token.contents.split()[0], syntax_help)
    m = re.search(r'for (.*?) (.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments, %s" % (tag_name, syntax_help)

    return GetCalendarNode(*m.groups())

class GetCalendarNode(template.Node):
    def __init__(self, month, year, var_name):
        self.year = template.Variable(year)
        self.month = template.Variable(month)
        self.var_name = var_name

    def render(self, context):
        mycal = Calendar()
        context[self.var_name] = mycal.monthdatescalendar(int(self.year.resolve(context)), int(self.month.resolve(context)))

        return ''
class CalendarHandler(webapp2.RequestHandler):
    def get(self):





class HomePageHandler(webapp2.RequestHandler):
    def get(self):






app = webapp2.WSGIApplication([
    ('/calendar', CalendarHandler),
    ('/', HomePageHandler),
], debug=True)



#    template= jinja_current_dir.get_template('my_blog.html')
#    self.response.write(template.render())
#    template_vars={'title': title, 'main': main, 'username':username}
#    template=jinja_current_dir.get_template('posts.html')
#    self.response.write(template.render(template_vars))
