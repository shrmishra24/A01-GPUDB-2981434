
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

class Search(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')
        if action == 'Search':
            geometryShader = "False"
            tesselationShader = "False"
            shaderInt16 = "False"
            sparseBinding = "False"
            textureCompressionETC2 = "False"
            vertexPipelineStoresAndAtomics ="False"

            geometryShader = bool(self.request.get('geometryShader'))
            tesselationShader = bool(self.request.get('tesselationShader'))
            shaderInt16 = bool(self.request.get('shaderInt16'))
            sparseBinding = bool(self.request.get('sparseBinding'))
            textureCompressionETC2 = bool(self.request.get('textureCompressionETC2'))
            vertexPipelineStoresAndAtomics = bool(self.request.get('vertexPipelineStoresAndAtomics'))

            gpu_fetched= gpuList.query()

            if geometryShader:
                gpu_fetched = gpu_fetched.filter(gpuList.geometryShader == True)
            if tesselationShader:
                gpu_fetched = gpu_fetched.filter(gpuList.tesselationShader == True)
            if shaderInt16:
                gpu_fetched = gpu_fetched.filter(gpuList.shaderInt16 == True)
    		if sparseBinding:
    			gpu_fetched = gpu_fetched.filter(gpuList.sparseBinding == True)
            if textureCompressionETC2:
                gpu_fetched = gpu_fetched.filter(gpuList.textureCompressionETC2 == True)
            if vertexPipelineStoresAndAtomics:
                gpu_fetched = gpu_fetched.filter(gpuList.vertexPipelineStoresAndAtomics == True)
            gpu_fetched = gpu_fetched.filter()      

            results_dict = {'logout_url' : users.create_logout_url(self.request.uri),
                            'gpuList':gpu_fetched
                            }


            template = JINJA_ENVIRONMENT.get_template('templates/searchResult.html')
            rendered_template = template.render(results_dict)
            self.response.write(rendered_template)
