import web
import os.path
from web import form
from graph.settings import UPLOADS
from graph.views.base import View

class Draw(View):
    def get(self, filename):
        return {'array': [[float(number) for number in line.split()] \
            for line in open(os.path.join(UPLOADS, filename))]}
