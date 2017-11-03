import typing
from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls
from apistar import typesystem


class Item(typesystem.Object):
    """
    Menu item schema
    """
    properties = {
        'id': typesystem.String,
        'name': typesystem.String,
        'price': typesystem.Number,
        'image': typesystem.String,
        'section': typesystem.String
    }

class Menu(typesystem.Object):
    """
    Menu schema
    """
    properties = {
        'id': typesystem.String,
        'name': typesystem.String,
        'description': typesystem.String
    }

def ping():
    """
    Healthcheck endpoint
    """
    return {'message': 'ok'}

def get_menu_by_id(menu_id: str) -> typing.List[Menu]:
    """
    Gets a specific menu by id
    """
    return Menu(name="my first menu", id=menu_id, description="The best first menu")

def get_items_for_menu(menu_id: str) -> typing.List[Item]:
    """
    Gets all of the items for the given menu_id
    """
    return [
        Item(id='1', name='A menu item', price=9.99, image='http://google.com', section='dessert')
    ]

routes = [
    Route('/menu/v1/menus/{menu_id}', 'GET', get_menu_by_id),
    Route('/menu/v1/menus/{menu_id}/items', 'GET', get_items_for_menu),
    Route('/healthz', 'GET', ping),
    Include('/docs', docs_urls)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.main()
