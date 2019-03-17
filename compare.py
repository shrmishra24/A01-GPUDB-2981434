
import datetime
import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
from datetime import datetime
from models.myuser import MyUser
from models.gpudb import gpuList


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class Compare(webapp2.RequestHandler):
    gpuName=""
    gpuName1=""
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        global gpuName
        global gpuName1
        action = self.request.get('button')
        user = users.get_current_user()
        if user == None:
            rendered_template = {
            'login_url' : users.create_login_url(self.request.uri)
            }
            template = JINJA_ENVIRONMENT.get_template('templates/mainpage_guest.html')
            self.response.write(template.render(rendered_template))
            return

        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()
        if myuser == None:
            myuser = MyUser(id=user.user_id())
            myuser.put()

        if action=='Compare':
            gpuName = self.request.get('gpuName')
            gpu_key = ndb.Key('gpuList', gpuName)
            gpu = gpu_key.get()

            gpuName1 = self.request.get('gpuName1')
            gpu_key1 = ndb.Key('gpuList', gpuName1)
            gpu1 = gpu_key1.get()

            template_values = {
            'logout_url' : users.create_logout_url(self.request.uri),
            'gpu' : gpu,
            'gpu1' : gpu1
            }
            template = JINJA_ENVIRONMENT.get_template('templates/compare.html')
            self.response.write(template.render(template_values))
