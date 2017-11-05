def test_restaurant_client_workflow(client_empty_db):
    # Create new restaurant
    response = client_empty_db.post('http://localhost/menu/v1/restaurants', json={
        'name': 'Cool place'
    })
    assert response.status_code == 201
    assert response.json()['name'] == 'Cool place'
    restaurant_id = response.json()['id']
    assert restaurant_id is not None

    # Change the name
    change_name_response = client_empty_db.put(f'http://localhost/menu/v1/restaurants/{restaurant_id}', json={
        'name': 'Better name'
    })
    assert change_name_response.status_code == 200
    assert change_name_response.json()['name'] == 'Better name'
    assert change_name_response.json()['id'] == restaurant_id

    # Add a menu
    add_menu_request = client_empty_db.post(f'http://localhost/menu/v1/restaurants/{restaurant_id}/menus', json={
        'name': 'A cool menu',
        'description': 'a really cool menu'
    })
    assert add_menu_request.status_code == 201
    assert add_menu_request.json()['name'] == 'A cool menu'
    assert add_menu_request.json()['description'] == 'a really cool menu'
    assert add_menu_request.json()['id'] is not None

    # Get the restaurant
    get_restaurant = client_empty_db.get(f'http://localhost/menu/v1/restaurants/{restaurant_id}')
    assert get_restaurant.status_code == 200
    assert get_restaurant.json()['name'] == 'Better name'


    # Delete restaurant
    delete_restaurant = client_empty_db.delete(f'http://localhost/menu/v1/restaurants/{restaurant_id}')
    assert delete_restaurant.status_code == 204