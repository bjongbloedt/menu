from apistar.backends import sqlalchemy_backend
from apistar.frameworks.wsgi import WSGIApp as App

from api.project.routes import routes
from api.project.settings import settings

app = App(
    routes=routes,
    settings=settings,
    commands=sqlalchemy_backend.commands,
    components=sqlalchemy_backend.components
)


if __name__ == '__main__':
    app.main()
