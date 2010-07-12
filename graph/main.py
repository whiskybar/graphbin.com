import web
from graph.views.upload import Create

urls = (
    '/', 'Create',
)

app = web.application(urls, globals(), autoreload=True)

if __name__ == "__main__":
    app.run()

