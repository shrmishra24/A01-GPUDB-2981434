import webapp2
from webapp2 import Route

app = webapp2.WSGIApplication([
    Route('/', handler = 'main.MainPage'),
    Route('/gpu', handler = 'main.GPUHandler'),
    Route('/view', handler = 'view.ViewPage'),
    Route('/edit', handler = 'edit.Edit'),
    Route('/features', handler = 'features.FeatureHandler'),
    Route('/compareForm', handler = 'compareForm.ComparePage'),
    Route('/compare', handler = 'compare.Compare'),
    Route('/searchFeatures', handler = 'searchFeatures.SearchFeatures'),
    Route('/search', handler = 'search.Search'),
],debug=True)
