from apistar.test import TestClient
from app import app, get_items_for_menu, get_menu_by_id, ping


def test_ping():
    """
    Test ping
    """
    data = ping()
    assert data == {'message': 'ok'}


def test_ping_request():
    """
    Test ping
    """
    client = TestClient(app)
    response = client.get('http://localhost/healthz')
    assert response.status_code == 200
    assert response.json() == {'message': 'ok'}


def test_get_menu_by_id():
    """
    Test getting a single menu
    """
    data = get_menu_by_id('1')
    assert data == {'id': '1', 'name': 'my first menu',
                    'description': 'The best first menu'}


def test_get_menu_by_id_request():
    """
    Test getting a single menu
    """
    client = TestClient(app)
    response = client.get('http://localhost/menu/v1/menus/3')
    assert response.status_code == 200
    assert response.json() ==\
        {'id': '3', 'name': 'my first menu', 'description': 'The best first menu'}


def test_get_items_for_menu():
    """
    Test getting all items for a menu
    """
    data = get_items_for_menu('1')
    assert data ==\
        [{'id': '1', 'name': 'A menu item', 'price': 9.99,
          'image': 'http://google.com', 'section': 'dessert'}]


def test_get_items_for_menu_request():
    """
    Test getting a single menu
    """
    client = TestClient(app)
    response = client.get('http://localhost/menu/v1/menus/1/items')
    assert response.status_code == 200
    assert response.json() ==\
        [{'id': '1', 'name': 'A menu item', 'price': 9.99,
          'image': 'http://google.com', 'section': 'dessert'}]
