import web
from web import form
from graph.settings import UPLOADS
from graph.views.base import View

class Draw(View):
    def get(self, filename):
        return {'array': [(1, 10), (2, 20), (3, 15)]}
