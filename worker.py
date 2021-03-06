import jinja2
import os
import webapp2
from google.appengine.api import taskqueue
from google.appengine.ext import db

class Counter(db.Model):
    count = db.IntegerProperty(indexed=False)

class CounterHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {'counters': Counter.all()}
        counter_template = jinja_environment.get_template('counter.html')
        self.response.out.write(counter_template.render(template_values))
    def post(self):
        key = self.request.get('key')

        # Add the task to the default queue.
        taskqueue.add(url='/worker', params={'key': key})

        self.redirect('/')

class CounterWorker(webapp2.RequestHandler):
    def post(self): # should run at most 1/s
        key = self.request.get('key')
        def txn():
            counter = Counter.get_by_key_name(key)
            if counter is None:
                counter = Counter(key_name=key, count=1)
            else:
                counter.count += 1
            counter.put()
        db.run_in_transaction(txn)

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
app = webapp2.WSGIApplication([('/', CounterHandler),
                              ('/worker', CounterWorker)],
                              debug=True)
