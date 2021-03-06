from apistar import environment, typesystem

from .models import Base


class Env(environment.Environment):
    """
    Environmental variables
    """
    properties = {
        'DEBUG': typesystem.boolean(default=False),
        'DATABASE_URL': typesystem.string(default='sqlite:///local.db')
    }


env = Env()


settings = {
    'DEBUG': env['DEBUG'],
    'DATABASE': {
        'URL': env['DATABASE_URL'],
        'METADATA': Base.metadata
    }
}
