def test_get_menu_by_id_request_should_return_NotFound_if_no_menu(client_empty_db):
    """
    Test getting a single menu
    """
    response = client_empty_db.get('http://localhost/menu/v1/menus/1234123')
    assert response.status_code == 404
    assert response.json() ==\
        {'message': 'menu with id 1234123 was not found'}


def test_get_items_for_menu_request(client_empty_db):
    """
    Test getting a single menu
    """
    response = client_empty_db.get('http://localhost/menu/v1/menus/1234123/items')
    assert response.status_code == 404
    assert response.json() ==\
        {'message': 'items for the menu with id 1234123 were not found'}


def test_get_menus_request(client_empty_db):
    """
    Test getting a single menu
    """
    response = client_empty_db.get('http://localhost/menu/v1/menus')
    assert response.status_code == 404
    assert response.json() ==\
        {'message': 'no menus were found'}

def test_ping_request(client_empty_db):
    """
    Test ping
    """
    response = client_empty_db.get('http://localhost/healthz')
    assert response.status_code == 200
    assert response.json() == {'message': 'ok'}

def test_add_menu_request(client_empty_db):
    """
    Test adding a menu
    """
    response = client_empty_db.post('http://localhost/menu/v1/menus', json={
        'name': 'test',
        'description': 'stuff'
    })
    assert response.status_code == 201

    assert response.json()['name'] == 'test'
    assert response.json()['description'] == 'stuff'