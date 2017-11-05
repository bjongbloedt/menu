from project.views import get_restaurant_by_id, add_restaurant, get_restaurants, update_restaurant_name, remove_restaurant, get_menus_for_restaurant
from project.models import RestaurantsModel, MenusModel
from project.schemas import RestaurantsSchema


def test_get_restaurant_by_id(db_session):
    """
    Test getting a single restaurant
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()

    data = get_restaurant_by_id(db_session, '1')
    assert data == {'id': '1', 'name': 'Cool place'}

def test_get_restaurant_by_id(db_session):
    """
    Test getting a single restaurant that doesn't exist
    """
    data = get_restaurant_by_id(db_session, '12345')
    assert data.status == 404
    assert data.content == {'message': 'restaurant with id 12345 was not found'}

def test_add_new_restaurant(db_session):
    """
    Test adding a new restaurant
    """
    data = add_restaurant(db_session, {'name': 'new restaurant'})
    assert data.status == 201
    assert data.content['name'] == 'new restaurant'

    query = db_session.query(RestaurantsModel).filter(RestaurantsModel.id == data.content['id']).first()
    assert query is not None

def test_add_new_restaurant_should_return_error_if_fields_are_missing(db_session):
    """
    Test adding a new restaurant checks the fields passed in
    """
    data = add_restaurant(db_session, {})
    assert data.status == 400
    assert data.content == {'message': 'restaurant request invalid'}

def test_get_restaurants_should_resturn_all_restaurants(db_session):
    db_session.add_all([
        RestaurantsModel(id='1', name='Cool place'),
        RestaurantsModel(id='2', name='Cool place'),
        RestaurantsModel(id='3', name='Cool place')
    ])
    db_session.commit()

    data = get_restaurants(db_session)
    assert len(data) == 3

def test_get_menus_should_return_NotFound_when_no_menus(db_session):
    """
    Test that NotFound is returned when there are no restaurants
    """
    data = get_restaurants(db_session)
    assert data.content == {'message': 'no restaurants were found'}

def test_put_update_restaurant_name_should_update_name(db_session):
    """
    Update restaurant with new name
    """
    db_session.add_all([
        RestaurantsModel(id='1', name='Cool place'),
        RestaurantsModel(id='2', name='Cool place'),
        RestaurantsModel(id='3', name='Cool place')
    ])
    db_session.commit()

    data = update_restaurant_name(db_session, '1', {'name': 'Another place'})
    assert data.status == 200
    assert data.content['name'] == 'Another place'

    query = db_session.query(RestaurantsModel).filter(RestaurantsModel.name == 'Another place').all()
    assert len(query) == 1

def test_put_update_restaurant_name_should_return_NotFound_when_id_is_bad(db_session):
    """
    Try to update non existent restaurant
    """
    db_session.add_all([
        RestaurantsModel(id='1', name='Cool place'),
        RestaurantsModel(id='2', name='Cool place'),
        RestaurantsModel(id='3', name='Cool place')
    ])
    db_session.commit()

    data = update_restaurant_name(db_session, '4', {'name': 'Another place'})
    assert data.status == 404
    assert data.content == {'message': 'unable to update restaurant 4 with name Another place'}

    query = db_session.query(RestaurantsModel).filter(RestaurantsModel.name == 'Another place').all()
    assert len(query) == 0

def test_put_update_restaurant_name_should_return_NotFound_name_is_empty(db_session):
    """
    Try to update non existent restaurant
    """
    db_session.add_all([
        RestaurantsModel(id='1', name='Cool place'),
        RestaurantsModel(id='2', name='Cool place'),
        RestaurantsModel(id='3', name='Cool place')
    ])
    db_session.commit()

    data = update_restaurant_name(db_session, '3', {'name': ''})
    assert data.status == 400
    assert data.content == {'message': 'unable to update restaurant 3 with name '}

    query = db_session.query(RestaurantsModel).filter(RestaurantsModel.name == '').all()
    assert len(query) == 0

def test_remove_restaurant_should_remove(db_session):
    """
    Try to remove restaurant
    """
    db_session.add_all([
        RestaurantsModel(id='1', name='Cool place'),
        RestaurantsModel(id='2', name='Cool place'),
        RestaurantsModel(id='3', name='Cool place')
    ])
    db_session.commit()

    data = remove_restaurant(db_session, '1')
    assert data.status == 204
    assert data.content == {}

    query = db_session.query(RestaurantsModel).filter(RestaurantsModel.id == 1).all()
    assert len(query) == 0

def test_remove_restaurant_should_not_remove_when_id_empty(db_session):
    """
    Try to remove restaurant
    """
    db_session.add_all([
        RestaurantsModel(id='1', name='Cool place'),
        RestaurantsModel(id='2', name='Cool place'),
        RestaurantsModel(id='3', name='Cool place')
    ])
    db_session.commit()

    data = remove_restaurant(db_session, '')
    assert data.status == 400
    assert data.content == {'message': 'must provide id'}

def test_remove_restaurant_should_not_remove_when_id_does_not_exist(db_session):
    """
    Try to remove restaurant
    """
    db_session.add_all([
        RestaurantsModel(id='1', name='Cool place'),
        RestaurantsModel(id='2', name='Cool place'),
        RestaurantsModel(id='3', name='Cool place')
    ])
    db_session.commit()

    data = remove_restaurant(db_session, '45')
    assert data.status == 404
    assert data.content == {'message': 'unable to delete restaurant 45'}

def test_get_menus_for_restaurant_should_return_menus(db_session):
    """
    Test getting all items for a menu
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    db_session.add_all([
        MenusModel(id="2", name="my first menu", description="The best first menu", restaurant_id="1"),
        MenusModel(id="3", name="my first menu", description="The best first menu", restaurant_id="1"),
        MenusModel(id="4", name="my first menu", description="The best first menu", restaurant_id="1")
    ])
    db_session.commit()

    data = get_menus_for_restaurant(db_session, '1')
    assert len(data.content) == 3

def test_get_menus_for_restaurant_should_return_error_if_menu_is_not_found(db_session):
    """
    Test getting all items for a menu
    """

    data = get_menus_for_restaurant(db_session, '50')
    assert data.status == 404
    assert data.content ==\
        {'message': 'menus for the restaurant with id 50 were not found'}

def test_get_menus_for_restaurant_should_return_empty_list_if_no_items_match_menu_id(db_session):
    """
    Test getting all items for a menu
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    db_session.add_all([
        MenusModel(id="2", name="my first menu", description="The best first menu", restaurant_id="1"),
        MenusModel(id="3", name="my first menu", description="The best first menu", restaurant_id="1"),
        MenusModel(id="4", name="my first menu", description="The best first menu", restaurant_id="1")
    ])
    db_session.commit()

    data = get_menus_for_restaurant(db_session, '12345')
    assert data.status == 404
    assert data.content ==\
        {'message': 'menus for the restaurant with id 12345 were not found'}
