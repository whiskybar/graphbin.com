import sys
import web
from graph.views.upload import Create
from graph.views.plot import Draw

urls = (
    '/', 'Create',
    '/(.+)/', 'Draw',
)

app = web.application(urls, globals(), autoreload=True)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'serve':
        from flup.server.fcgi import WSGIServer
        WSGIServer(
            application=app.wsgifunc(),
            bindAddress='/tmp/graph.socket',
        ).run()
    else:
        app.run()

