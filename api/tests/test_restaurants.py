from project.views import get_restaurant_by_id, add_restaurant, get_restaurants, update_restaurant_name
from project.models import RestaurantsModel
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

    data = update_restaurant_name(db_session, '1', 'Another place')
    assert data.status == 200
    assert data.content['name'] == 'Another place'

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

    data = update_restaurant_name(db_session, '4', 'Another place')
    assert data.status == 404
    assert data.content == {'message': 'unable to update restaurant 4 with name Another place'}

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

    data = update_restaurant_name(db_session, '3', '')
    assert data.status == 400
    assert data.content == {'message': 'unable to update restaurant 3 with name '}