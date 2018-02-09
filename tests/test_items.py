from ..project.models import MenusModel, ItemsModel, RestaurantsModel
from ..project.views import add_item_to_menu, remove_item, get_item_by_id


def test_add_new_item_should_create_new_menu(db_session):
    """
    Test that a new item can be added
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="12345", name="my first menu",
                      description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()

    req = {'name': 'Sandwich', 'price': 11.99,
           'image': 'http://image.com/image', 'section': 'desserts'}
    data = add_item_to_menu(db_session, '12345', req)
    assert data.status == 201
    assert data.content['name'] == 'Sandwich'
    assert data.content['price'] == 11.99
    assert data.content['image'] == 'http://image.com/image'
    assert data.content['section'] == 'desserts'
    assert data.content['menu_id'] == "12345"
    assert data.content['id'] is not None

    query = db_session.query(ItemsModel).filter(
        ItemsModel.id == data.content['id']).first()
    assert query is not None


def test_add_new_item_should_return_invalid_when_request_is_incorrect(db_session):
    """
    Test that a new item can't be added when request is invalid
    """
    data = add_item_to_menu(db_session, "1", {})
    assert data.status == 400
    assert data.content == {'message': 'item request invalid'}


def test_remove_item_should_remove(db_session):
    """
    Try to remove item
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="12345", name="my first menu",
                      description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()
    item = ItemsModel(id="54321", name="sandwich one", price=9.99,
                      image="http://image.com/image", section="sandwiches", menu_id="12345")
    db_session.add(item)
    db_session.commit()

    data = remove_item(db_session, '54321')
    assert data.status == 204
    assert data.content == {}

    query = db_session.query(ItemsModel).filter(ItemsModel.id == "54321").all()
    assert len(query) == 0


def test_remove_item_should_not_remove_when_id_empty(db_session):
    """
    Try to remove item
    """
    data = remove_item(db_session, '')
    assert data.status == 400
    assert data.content == {'message': 'must provide id'}


def test_remove_item_should_not_remove_when_id_does_not_exist(db_session):
    """
    Try to remove item
    """
    data = remove_item(db_session, '45')
    assert data.status == 404
    assert data.content == {'message': 'unable to delete item 45'}


def test_get_item_by_id(db_session):
    """
    Test getting a single item
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="1", name="my first menu",
                      description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()
    item = ItemsModel(id="54321", name="sandwich one", price=9.99,
                      image="http://image.com/image", section="sandwiches", menu_id="1")
    db_session.add(item)
    db_session.commit()

    data = get_item_by_id(db_session, '54321')
    assert data.status == 200
    assert data.content == {'id': '54321', 'name': 'sandwich one', 'price': 9.99,
                            'image': 'http://image.com/image', 'section': 'sandwiches', 'menu_id': '1'}


def test_get_item_by_id_should_return_error(db_session):
    """
    Test getting a single item
    """
    data = get_item_by_id(db_session, '1234123')
    assert data.status == 404
    assert data.content ==\
        {'message': 'item with id 1234123 was not found'}
