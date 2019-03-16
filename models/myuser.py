from google.appengine.ext import ndb
from gpudb import gpuList
class MyUser(ndb.Model):
    #username = ndb.StringProperty()
    gpu_fetched = ndb.StructuredProperty(gpuList, repeated=True)
