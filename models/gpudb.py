from google.appengine.ext import ndb

class gpuList(ndb.Model):
    gpuName = ndb.StringProperty(required = True)
    manufacturer = ndb.StringProperty()
    dateIssued = ndb.DateProperty()
    geometryShader = ndb.BooleanProperty()
    tesselationShader = ndb.BooleanProperty()
    shaderInt16 = ndb.BooleanProperty()
    sparseBinding = ndb.BooleanProperty()
    textureCompressionETC2 = ndb.BooleanProperty()
    vertexPipelineStoresAndAtomics = ndb.BooleanProperty()
