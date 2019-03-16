
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
        if action=='Compare':
            gpuName = self.request.get('gpuName')
            gpu_key = ndb.Key('gpuList', gpuName)
            gpu = gpu_key.get()

            gpuName1 = self.request.get('gpuName1')
            gpu_key1 = ndb.Key('gpuList', gpuName1)
            gpu1 = gpu_key1.get()

            template_values = {
            'gpu' : gpu,
            'gpu1' : gpu1
            }
            template = JINJA_ENVIRONMENT.get_template('templates/compare.html')
            self.response.write(template.render(template_values))
