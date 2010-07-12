import web
from graph.settings import TEMPLATES

class View(object):
    def render(self, result):
        render = web.template.render(TEMPLATES)
        page = getattr(render, self.__class__.__name__.lower())
        return render.base(page(**result))  

    def get(self, *args, **kwargs):
        pass

    def GET(self, *args, **kwargs):
        result = self.get(*args, **kwargs)
        if result is None:
            result = {}
        if isinstance(result, dict):
            return self.render(result)

    def POST(self, *args, **kwargs):
        result = self.post(*args, **kwargs)
        if result is None:
            result = {}
        if isinstance(result, basestring):
            raise web.seeother(result)
        if isinstance(result, dict):
           return self.render(result)


