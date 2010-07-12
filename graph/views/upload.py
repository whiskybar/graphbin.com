from tempfile import NamedTemporaryFile
import web
from web import form
from graph.settings import UPLOADS
from graph.views.base import View

class Create(View):
    def post(self):
        csv = NamedTemporaryFile(suffix='.csv', dir=UPLOADS, delete=False)
        csv.write(web.input()['csvfile'])
        csv.close()
        return '/'
 
