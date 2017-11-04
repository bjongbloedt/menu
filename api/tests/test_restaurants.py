import json
from project.views import get_restaurant_by_id
from project.models import RestaurantsModel
from project.schemas import RestaurantsSchema


def test_get_menu_by_id(db_session):
    """
    Test getting a single restaurant
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()

    data = get_restaurant_by_id(db_session, '1')
    assert data == {'id': '1', 'name': 'Cool place'}

def test_get_menu_by_id(db_session):
    """
    Test getting a single restaurant that doesn't exist
    """
    data = get_restaurant_by_id(db_session, '12345')
    assert data.status == 404
    assert data.content == {'message': 'restaurant with id 12345 was not found'}