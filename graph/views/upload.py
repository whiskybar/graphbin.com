from tempfile import NamedTemporaryFile
from os.path import basename
import web
from web import form
from graph.settings import UPLOADS
from graph.views.base import View

class Create(View):
    def post(self):
        csv = NamedTemporaryFile(prefix='', dir=UPLOADS, delete=False)
        csv.write(web.input()['csvfile'])
        csv.close()
        return '/%s/' % basename(csv.name)
 
