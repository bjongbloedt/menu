from apistar import Include, Route
from apistar.handlers import docs_urls
from project.views import get_items_for_menu, get_menu_by_id, ping


routes = [
    Route('/menu/v1/menus/{menu_id}', 'GET', get_menu_by_id),
    Route('/menu/v1/menus/{menu_id}/items', 'GET', get_items_for_menu),
    Route('/healthz', 'GET', ping),
    Include('/docs', docs_urls)
]