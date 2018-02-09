def test_item_client_workflow(client_empty_db):
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

    # Create new item
    create_item_response = client_empty_db.post(f'http://localhost/menu/v1/menus/{menu_id}/items', json={
        'name': 'root beer',
        'price': 1.99,
        'image': 'http://image-of-rootbeer.net',
        'section': 'drinks'
    })
    assert create_item_response.status_code == 201
    assert create_item_response.json()['name'] == 'root beer'
    assert create_item_response.json()['price'] == 1.99
    assert create_item_response.json(
    )['image'] == 'http://image-of-rootbeer.net'
    assert create_item_response.json()['section'] == 'drinks'
    item_id = create_item_response.json()['id']
    assert item_id is not None

    # Get items by menu
    get_items_by_menu = client_empty_db.get(
        f'http://localhost/menu/v1/menus/{menu_id}/items')
    assert get_items_by_menu.status_code == 200
    assert len(get_items_by_menu.json()) == 1

    # Get item
    get_item = client_empty_db.get(f'http://localhost/menu/v1/items/{item_id}')
    assert get_item.status_code == 200
    assert get_item.json()['name'] == 'root beer'
    assert get_item.json()['price'] == 1.99
    assert get_item.json()['image'] == 'http://image-of-rootbeer.net'
    assert get_item.json()['section'] == 'drinks'
    assert get_item.json()['id'] == item_id

    # Delete Item
    remove_item_response = client_empty_db.delete(
        f'http://localhost/menu/v1/items/{item_id}')
    assert remove_item_response.status_code == 204
