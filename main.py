
import datetime
import webapp2
import jinja2
import os
import logging
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

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
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

        gpu_fetched= gpuList.query().order(gpuList.gpuName).fetch()

        if gpu_fetched:
            results_dict = {'logout_url' : users.create_logout_url(self.request.uri),
                            'gpuList':gpu_fetched}
        else:
            results_dict = {'logout_url' : users.create_logout_url(self.request.uri)}

        # results_dict = {'logout_url' : users.create_logout_url(self.request.uri),
        #                  'gpuList': myuser.gpu_fetched}

        template = JINJA_ENVIRONMENT.get_template('templates/crud.html')
        rendered_template = template.render(results_dict)
        self.response.write(rendered_template)

class GPUHandler(webapp2.RequestHandler):
    def post(self):
        action = self.request.get('button')
        if action == 'Save':
            gpuName = self.request.get('gpuName')
            manufacturer = self.request.get('manufacturer')
            dateIssued = datetime.strptime(self.request.get('dateIssued'), '%Y-%m-%d')
            geometryShader = self.request.get('geometryShader')=='on'
            tesselationShader = self.request.get('tesselationShader')=='on'
            shaderInt16 = self.request.get('shaderInt16')=='on'
            sparseBinding = self.request.get('sparseBinding')=='on'
            textureCompressionETC2 = self.request.get('textureCompressionETC2')=='on'
            vertexPipelineStoresAndAtomics = self.request.get('vertexPipelineStoresAndAtomics')=='on'

            user = users.get_current_user()
            myuser_key = ndb.Key('MyUser', user.user_id())
            myuser = myuser_key.get()

            gpu_key = ndb.Key('gpu_fetched', gpuName)
            gpus = gpu_key.get()

            # if gpus is None:
            gpu_values_stored_in_db = gpuList(gpuName = gpuName, manufacturer=manufacturer,dateIssued=dateIssued,
                                geometryShader= geometryShader,
                                tesselationShader = tesselationShader,
                                shaderInt16 = shaderInt16,
                                sparseBinding =sparseBinding,
                                textureCompressionETC2 = textureCompressionETC2,
                                vertexPipelineStoresAndAtomics = vertexPipelineStoresAndAtomics, id = gpuName)
            gpu_values_stored_in_db.put()
            myuser.gpu_fetched.append(gpu_values_stored_in_db)
            myuser.put()
            self.redirect('/')
        elif action == 'View':
             self.redirect('/view')
        elif action == 'Compare':
            self.redirect('/compareForm')
        elif action == 'Feature Search':
            self.redirect('/searchFeatures')
