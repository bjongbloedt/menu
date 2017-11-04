from apistar.frameworks.wsgi import WSGIApp as App
from apistar.backends import sqlalchemy_backend
from project.routes import routes
from project.models import Base


settings = {
    "DATABASE": {
        "URL": "sqlite:///test.db",
        "METADATA": Base.metadata
    }
}


app = App(
    routes=routes,
    settings=settings,
    commands=sqlalchemy_backend.commands,
    components=sqlalchemy_backend.components
)


if __name__ == '__main__':
    app.main()
