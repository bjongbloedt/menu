from apistar import Include, Route
from apistar.handlers import docs_urls
from project.views import (
    get_items_for_menu,
    get_menu_by_id,
    get_menus, ping,
    add_menu_to_restaurant,
    get_restaurant_by_id,
    add_restaurant,
    get_restaurants,
    update_restaurant_name,
    remove_restaurant,
    update_menu,
    remove_menu,
    add_item_to_menu,
    get_menus_for_restaurant,
    remove_item,
    get_item_by_id
)

restaurants_routes = [
    Route('/{rest_id}/menus', 'POST', add_menu_to_restaurant),
    Route('/{restaurant_id}/menus', 'GET', get_menus_for_restaurant),
    Route('/{restaurant_id}', 'GET', get_restaurant_by_id),
    Route('', 'GET', get_restaurants),
    Route('/{restaurant_id}', 'PUT', update_restaurant_name),
    Route('', 'POST', add_restaurant),
    Route('/{restaurant_id}', 'DELETE', remove_restaurant)
]

menus_routes = [
    Route('/{menu_id}', 'GET', get_menu_by_id),
    Route('', 'GET', get_menus),
    Route('/{menu_id}/items', 'GET', get_items_for_menu),
    Route('/{menu_id}/items', 'POST', add_item_to_menu),
    Route('/{menu_id}', 'PUT', update_menu),
    Route('/{menu_id}', 'DELETE', remove_menu)
]

items_routes = [
    Route('/{item_id}', 'DELETE', remove_item),
    Route('/{item_id}', 'GET', get_item_by_id)

]

routes = [
    Route('/healthz', 'GET', ping),
    Include('/docs', docs_urls),
    Include('/menu/v1/restaurants', restaurants_routes),
    Include('/menu/v1/menus', menus_routes),
    Include('/menu/v1/items', items_routes)
]
