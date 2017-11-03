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
    assert data == {'message': 'Got menu 1'}

def test_get_menu_by_id_request():
    """
    Test getting a single menu
    """
    client = TestClient(app)
    response = client.get('http://localhost/menu/v1/menus/1')
    assert response.status_code == 200
    assert response.json() == {'message': 'Got menu 1'}

def test_get_items_for_menu():
    """
    Test getting all items for a menu
    """
    data = get_items_for_menu('1')
    assert data == {'message': 'Got items for menu 1'}

def test_get_menu_by_id_request():
    """
    Test getting a single menu
    """
    client = TestClient(app)
    response = client.get('http://localhost/menu/v1/menus/1/items')
    assert response.status_code == 200
    assert response.json() == {'message': 'Got items for menu 1'}