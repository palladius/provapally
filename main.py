#!/usr/bin/env python

# 2.7

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


import webapp2
import jinja2
import os

from todo import Todo

VERSION = '0.0.8' # TODO copy from file
APPID   = 's~provapally'
APPNAME = 'ProvaPally'

#class MainHandler(webapp2.RequestHandler):
#    def get(self):
#        self.response.out.write('Hello world (Riccardo @ Provapally)!')

#app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)

class TodosPage(webapp.RequestHandler):
    def get(self):
      user = users.get_current_user()
      if user:
        names = ['To', 'Do' ,  user.nickname() ]
      else:
        names = ['To', 'Do' , 'No user' ]
      template_data = {
        'names': names,
        'version': VERSION,
        'user': user,
        'page': 'todos',
        'appid': APPID,
        'appname': APPNAME,
        'todos': [ t.__str__() for t in Todo.getAll()],
      }
      t = Todo.createTodo('Todos Index REMOVE ME at every index...')
      #if user:
      #    self.response.headers['Content-Type'] = 'text/plain'
      #    self.response.out.write('[ProvaPally Obsolete]: Groezi Mittenand, liebe gaeste' + user.nickname())
      #else:
      #    self.redirect(users.create_login_url(self.request.uri))
      jinja_environment = jinja2.Environment( loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
      template = jinja_environment.get_template('todos-index.html')
      self.response.write(template.render(template_data))

class MainPage(webapp.RequestHandler):
    def get(self):
      user = users.get_current_user()
      if user:
        names = ['Ricc', 'Alessandro' ,  user.nickname() ]
      else:
        names = ['Ricc', 'Alessandro' , 'No user' ]
      template_data = {
        'names': names,
        'version': VERSION,
        'user': user,
        'page': 'main',
        'appid': APPID,
        'appname': APPNAME,
      }
      #if user:
      #    self.response.headers['Content-Type'] = 'text/plain'
      #    self.response.out.write('[ProvaPally Obsolete]: Groezi Mittenand, liebe gaeste' + user.nickname())
      #else:
      #    self.redirect(users.create_login_url(self.request.uri))
      jinja_environment = jinja2.Environment( loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
      template = jinja_environment.get_template('index.html')
      self.response.write(template.render(template_data))

app = webapp.WSGIApplication( [
   ('/', MainPage),
   ('/todos/', TodosPage),
   #('/projects', MainPage),
  ], debug=True )

#app.response.write(template.render())
