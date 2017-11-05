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

def test_menu_client_workflow(client_empty_db):
    # Create new restaurant
    response = client_empty_db.post('http://localhost/menu/v1/restaurants', json={
        'name': 'Cool place'
    })
    assert response.status_code == 201
    assert response.json()['name'] == 'Cool place'
    restaurant_id = response.json()['id']
    assert restaurant_id is not None

    # Create new menu
    create_menu_response = client_empty_db.post(f'http://localhost/menu/v1/restaurants/{restaurant_id}/menus', json={
        'name': 'Cool place, first menu',
        'description': 'A really great menu'
    })
    assert create_menu_response.status_code == 201
    assert create_menu_response.json()['name'] == 'Cool place, first menu'
    assert create_menu_response.json()['description'] == 'A really great menu'
    menu_id = create_menu_response.json()['id']
    assert menu_id is not None

    # Change the name
    change_name_response = client_empty_db.put(f'http://localhost/menu/v1/menus/{menu_id}', json={
        'name': 'Better name'
    })
    assert change_name_response.status_code == 200
    assert change_name_response.json()['name'] == 'Better name'
    assert create_menu_response.json()['description'] == 'A really great menu'
    assert change_name_response.json()['id'] == menu_id

    # Add a item
    add_item_request = client_empty_db.post(f'http://localhost/menu/v1/menus/{menu_id}/items', json={
        'name': 'Really nice cake',
        'price': 9.99,
        'image': 'http://image.com/image',
        'section': 'desserts'
    })
    assert add_item_request.status_code == 201
    assert add_item_request.json()['name'] == 'Really nice cake'
    assert add_item_request.json()['price'] == 9.99
    assert add_item_request.json()['image'] == 'http://image.com/image'
    assert add_item_request.json()['menu_id'] == menu_id
    assert add_item_request.json()['id'] is not None

    # Get the menu
    get_menu = client_empty_db.get(f'http://localhost/menu/v1/menus/{menu_id}')
    assert get_menu.status_code == 200
    assert get_menu.json()['name'] == 'Better name'
    assert get_menu.json()['description'] == 'A really great menu'
    assert get_menu.json()['id'] == menu_id

    # Delete menu
    delete_menu = client_empty_db.delete(f'http://localhost/menu/v1/menus/{menu_id}')
    assert delete_menu.status_code == 204
    