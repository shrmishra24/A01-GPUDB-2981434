
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
class Edit(webapp2.RequestHandler):
    gpuName = ""
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        global gpuName
        gpuName = self.request.get('gpuName')
        print("the gpu name is " +gpuName)
        gpu_key = ndb.Key('gpuList', gpuName)
        gpu = gpu_key.get()

        template_values = {
        'gpu' : gpu
        }

        template = JINJA_ENVIRONMENT.get_template('templates/edit.html')
        self.response.write(template.render(template_values))

    def post(self):
         action = self.request.get('button')
         if action == 'Update':

             gpu_key = ndb.Key('gpuList', gpuName)
             gpu = gpu_key.get()

             gpu.manufacturer = self.request.get('manufacturer')
             gpu.dateIssued = datetime.strptime(self.request.get('dateIssued'), '%Y-%m-%d')
             gpu.geometryShader = bool(self.request.get('geometryShader'))
             gpu.tesselationShader = bool(self.request.get('tesselationShader'))
             gpu.shaderInt16 = bool(self.request.get('shaderInt16'))
             gpu.sparseBinding = bool(self.request.get('sparseBinding'))
             gpu.textureCompressionETC2 = bool(self.request.get('textureCompressionETC2'))
             gpu.vertexPipelineStoresAndAtomics = bool(self.request.get('vertexPipelineStoresAndAtomics'))
             gpu.put()

             self.redirect('/view')
         elif action == 'Cancel':
            self.redirect('/view')
