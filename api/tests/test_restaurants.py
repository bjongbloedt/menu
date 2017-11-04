from project.views import get_restaurant_by_id, add_restaurant
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

def test_add_new_restuarant(db_session):
    """
    Test adding a new restaurant
    """
    data = add_restaurant(db_session, {'name': 'new restaurant'})
    assert data.status == 201
    assert data.content['name'] == 'new restaurant'

def test_add_new_restuarant_should_return_error_if_fields_are_missing(db_session):
    """
    Test adding a new restaurant checks the fields passed in
    """
    data = add_restaurant(db_session, {})
    assert data.status == 400
    assert data.content == {'message': 'restaurant request invalid'}