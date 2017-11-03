from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls

def ping():
    """
    Healthcheck endpoint
    """
    return {'message': 'ok'}

def get_menu_by_id(menu_id):
    """
    Gets a specific menu by id
    """
    return {'message': f'Got menu {menu_id}'}

def get_items_for_menu(menu_id):
    """
    Gets all of the items for the given menu_id
    """
    return {'message': f'Got items for menu {menu_id}'}

routes = [
    Route('/menu/v1/menus/{menu_id}', 'GET', get_menu_by_id),
    Route('/menu/v1/menus/{menu_id}/items', 'GET', get_items_for_menu),
    Route('/healthz', 'GET', ping),
    Include('/docs', docs_urls)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.main()
