from apistar.test import TestClient
from app import app

def test_get_menu_by_id_request_should_return_NotFound_if_no_menu():
    """
    Test getting a single menu
    """
    client = TestClient(app)
    response = client.get('http://localhost/menu/v1/menus/1234123')
    assert response.status_code == 404
    assert response.json() ==\
        {'message': 'menu with id 1234123 was not found'}


def test_get_items_for_menu_request():
    """
    Test getting a single menu
    """
    client = TestClient(app)
    response = client.get('http://localhost/menu/v1/menus/1234123/items')
    assert response.status_code == 404
    assert response.json() ==\
        {'message': 'items for the menu with id 1234123 were not found'}


def test_ping_request():
    """
    Test ping
    """
    client = TestClient(app)
    response = client.get('http://localhost/healthz')
    assert response.status_code == 200
    assert response.json() == {'message': 'ok'}