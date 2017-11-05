from project.models import MenusModel, ItemsModel, RestaurantsModel
from project.schemas import MenusSchema, ItemsSchema, AddMenuRequestSchema
from project.views import add_item_to_menu


def test_add_new_item_should_create_new_menu(db_session):
    """
    Test that a new item can be added
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="12345", name="my first menu", description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()

    req = {'name': 'Sandwich', 'price': 11.99, 'image': 'http://image.com/image', 'section': 'desserts'}
    data = add_item_to_menu(db_session, '12345', req)
    assert data.status == 201
    assert data.content['name'] == 'Sandwich'
    assert data.content['price'] == 11.99
    assert data.content['image'] == 'http://image.com/image'
    assert data.content['section'] == 'desserts'
    assert data.content['menu_id'] == "12345"
    assert data.content['id'] is not None

    query = db_session.query(ItemsModel).filter(ItemsModel.id == data.content['id']).first()
    assert query is not None


def test_add_new_item_should_return_invalid_when_request_is_incorrect(db_session):
    """
    Test that a new item can't be added when request is invalid
    """
    data = add_item_to_menu(db_session, "1", {})
    assert data.status == 400
    assert data.content == {'message': 'item request invalid'}