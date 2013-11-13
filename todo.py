"""Model ToDo"""

#import  google.appengine.ext.db
from google.appengine.ext import db
from google.appengine.api import users

import datetime


class Todo(db.Model):
  #owner = db.User(auto_current_user_add=True)
  created = db.DateTimeProperty(auto_now_add=True)
  priority = db.IntegerProperty()
  title = db.TextProperty()
  description = db.TextProperty()
  due = db.DateProperty()
  active = db.BooleanProperty(default=True)
  # See: https://developers.google.com/appengine/docs/python/datastore/datamodeling

  @staticmethod
  def createTodo(klass, title='Some Default Title'):
    """We create a new ToDo item and put it in the datastore.
    """
    #PythonJava
    my_todo = Todo(
        priority=5,
        title=title,
        description='Fix that leaky faucet 2',
        active=True,
        due=datetime.date(2009, 8, 7))
    my_todo.put()

  @staticmethod
  def getAll():
    """Retrieves all of those with priiority 5 for instance.

    See https://developers.google.com/appengine/docs/python/users/userobjects
    """
    #q = db.GqlQuery("SELECT * FROM Todo WHERE priority = :1", 5)
    #q = db.GqlQuery("SELECT * FROM Todo", distinct=True).filter('priority >', 2).order('title')
    q = Todo.all()
    q.fetch(1000)
    return [x for x in q] # materializes them
    #index_list = q.index_list()
    #for ix in index_list:
    #todos = q.get()
    #return index_list
    #return todos

  def __str__(self):
     """Redefining toString()"""
     return "Todo('{title}')".format(title=self.title)

# taken from: https://developers.google.com/appengine/articles/life_of_write

