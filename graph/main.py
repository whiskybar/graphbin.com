import web
from graph.views.upload import Create
from graph.views.plot import Draw

urls = (
    '/', 'Create',
    '/(.+)/', 'Draw',
)

app = web.application(urls, globals(), autoreload=True)

if __name__ == "__main__":
    app.run()

