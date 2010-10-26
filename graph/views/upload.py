import re
import json
from tempfile import NamedTemporaryFile
from os.path import basename

import web
from web import form

from graph.settings import UPLOADS
from graph.views.base import View


class Create(View):

    split_re = re.compile('[^0-9.+-]*')

    def process_input(self, f):
        for line in f:
            serie = filter(None, self.split_re.split(line))
            try:
                if len(serie) > 1:
                    yield [float(serie[0]), float(serie[1])]
                elif len(serie) == 1:
                    yield float(serie[0])
            except ValueError:
                continue

    def post(self):
        with NamedTemporaryFile(prefix='', dir=UPLOADS, delete=False) as f:
            json.dump(list(self.process_input(web.input(csvfile={})['csvfile'].file)), f)
        return '/%s/' % basename(f.name)

