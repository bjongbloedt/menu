from apistar import Include, Route
from apistar.handlers import docs_urls
from project.views import get_items_for_menu, get_menu_by_id, get_menus, ping, add_menu_to_restaurant, get_restaurant_by_id


routes = [
    Route('/menu/v1/menus/{menu_id}', 'GET', get_menu_by_id),
    Route('/menu/v1/menus', 'GET', get_menus),
    Route('/menu/v1/menus/{menu_id}/items', 'GET', get_items_for_menu),
    Route('/menu/v1/restaurants/{rest_id}/menus', 'POST', add_menu_to_restaurant),
    Route('/menu/v1/restaurants/{restaurant_id}', 'GET', get_restaurant_by_id),
    Route('/healthz', 'GET', ping),
    Include('/docs', docs_urls)
]