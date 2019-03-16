
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

class FeatureHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        global gpuName
        gpuName = self.request.get('gpuName')
        gpu_key = ndb.Key('gpuList', gpuName)
        gpu = gpu_key.get()
        template_values = {
        'gpu' : gpu
        }
        template = JINJA_ENVIRONMENT.get_template('templates/features.html')
        self.response.write(template.render(template_values))
