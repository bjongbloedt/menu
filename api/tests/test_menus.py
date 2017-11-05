from project.models import MenusModel, ItemsModel, RestaurantsModel
from project.schemas import MenusSchema, ItemsSchema, AddMenuRequestSchema
from project.views import (
    get_items_for_menu,
    get_menu_by_id,
    ping,
    get_menus,
    add_menu_to_restaurant,
    update_menu,
    remove_menu
)


def test_get_menu_by_id(db_session):
    """
    Test getting a single menu
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="1", name="my first menu", description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()

    data = get_menu_by_id(db_session, '1')
    assert data.status == 200
    assert data.content == {'id': '1', 'name': 'my first menu',
                    'description': 'The best first menu',
                    'restaurant_id': '1'}

def test_get_menu_by_id_should_return_error(db_session):
    """
    Test getting a single menu
    """
    data = get_menu_by_id(db_session, '1234123')
    assert data.status == 404
    assert data.content ==\
        {'message': 'menu with id 1234123 was not found'}


def test_get_items_for_menu_should_return_items_on_menu(db_session):
    """
    Test getting all items for a menu
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="2", name="my first menu", description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()
    item = ItemsModel(id="1", name='A menu item', price=9.99, image="http://google.com", section="dessert", menu_id="2")
    db_session.add(item)
    db_session.commit()
    itemtwo = ItemsModel(id="3", name='A menu item', price=9.99, image="http://google.com", section="dessert", menu_id="3")
    db_session.add(itemtwo)
    db_session.commit()

    data = get_items_for_menu(db_session, '2')
    assert data.status == 200
    assert data.content ==\
        [{'id': '1', 'name': 'A menu item', 'price': 9.99,
          'image': 'http://google.com', 'section': 'dessert', 'menu_id': '2'}]

def test_get_items_for_menu_should_return_error_if_menu_is_not_found(db_session):
    """
    Test getting all items for a menu
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="2", name="my first menu", description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()
    item = ItemsModel(id="1", name='A menu item', price=9.99, image="http://google.com", section="dessert", menu_id="2")
    db_session.add(item)
    db_session.commit()
    itemtwo = ItemsModel(id="3", name='A menu item', price=9.99, image="http://google.com", section="dessert", menu_id="3")
    db_session.add(itemtwo)
    db_session.commit()

    data = get_items_for_menu(db_session, '50')
    assert data.content ==\
        {'message': 'items for the menu with id 50 were not found'}

def test_get_items_for_menu_should_return_empty_list_if_no_items_match_menu_id(db_session):
    """
    Test getting all items for a menu
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="12345", name="my first menu", description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()
    item = ItemsModel(id="1", name='A menu item', price=9.99, image="http://google.com", section="dessert", menu_id="3")
    db_session.add(item)
    db_session.commit()
    itemtwo = ItemsModel(id="3", name='A menu item', price=9.99, image="http://google.com", section="dessert", menu_id="3")
    db_session.add(itemtwo)
    db_session.commit()

    data = get_items_for_menu(db_session, '12345')
    assert data.content ==\
        {'message': 'items for the menu with id 12345 were not found'}


def test_get_menus_should_return_all_menus(db_session):
    """
    Test that all menus are returned
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    db_session.add_all([
        MenusModel(id="12345", name="my first menu", description="The best first menu", restaurant_id="1"),
        MenusModel(id="54321", name="my first menu", description="The best first menu", restaurant_id="1")
    ])
    db_session.commit()

    data = get_menus(db_session)
    assert data.status == 200
    assert len(data.content) == 2


def test_get_menus_should_return_NotFound_when_no_menus(db_session):
    """
    Test that NotFound is returned when there are no menus 
    """
    data = get_menus(db_session)
    assert data.content == {'message': 'no menus were found'}


def test_add_new_menu_should_create_new_menu(db_session):
    """
    Test that a new menu can be added
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()

    data = add_menu_to_restaurant(db_session, '1', {'name': 'new menu', 'description': 'A new menu'})
    assert data.status == 201
    assert data.content['name'] == 'new menu'
    assert data.content['description'] == 'A new menu'

    query = db_session.query(MenusModel).filter(MenusModel.id == data.content['id']).first()
    assert query is not None


def test_add_new_menu_should_return_invalid_when_request_is_incorrect(db_session):
    """
    Test that a new menu can be added
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()

    data = add_menu_to_restaurant(db_session, "1", {})
    assert data.status == 400
    assert data.content == {'message': 'menu request invalid'}

def test_put_menu_should_update_menu_name_and_decription(db_session):
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="12345", name="my first menu", description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()

    data = update_menu(db_session, "12345", {'name': 'updated menu', 'description': 'an updated menu'})
    assert data.status == 200
    assert data.content['name'] == 'updated menu'
    assert data.content['description'] == 'an updated menu'

    query = db_session.query(MenusModel).filter(MenusModel.id == '12345').first()
    assert query.name == 'updated menu'
    assert query.description == 'an updated menu'

def test_put_menu_should_update_menu_name(db_session):
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="12345", name="my first menu", description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()

    data = update_menu(db_session, "12345", {'name': 'updated menu'})
    assert data.status == 200
    assert data.content['name'] == 'updated menu'
    assert data.content['description'] == 'The best first menu'

    query = db_session.query(MenusModel).filter(MenusModel.id == '12345').first()
    assert query.name == 'updated menu'
    assert query.description == 'The best first menu'

def test_put_menu_should_update_menu_description(db_session):
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="12345", name="my first menu", description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()

    data = update_menu(db_session, "12345", {'description': 'updated'})
    assert data.status == 200
    assert data.content['name'] == 'my first menu'
    assert data.content['description'] == 'updated'

    query = db_session.query(MenusModel).filter(MenusModel.id == '12345').first()
    assert query.name == 'my first menu'
    assert query.description == 'updated'

def test_put_menu_should_return_error_when_no_field_to_update_is_provided(db_session):
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="12345", name="my first menu", description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()

    data = update_menu(db_session, "12345", {})
    assert data.status == 400
    assert data.content == {'message': 'unable to update menu 12345 without name or description provided'}

    query = db_session.query(MenusModel).filter(MenusModel.id == '12345').first()
    assert query.name == 'my first menu'
    assert query.description == 'The best first menu'

def test_remove_menu_should_remove(db_session):
    """
    Try to remove menu
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="12345", name="my first menu", description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()

    data = remove_menu(db_session, '12345')
    assert data.status == 204
    assert data.content == {}

    query = db_session.query(MenusModel).filter(MenusModel.id == "12345").all()
    assert len(query) == 0

def test_remove_menu_should_not_remove_when_id_empty(db_session):
    """
    Try to remove menu
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="12345", name="my first menu", description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()

    data = remove_menu(db_session, '')
    assert data.status == 400
    assert data.content == {'message': 'must provide id'}

def test_remove_menu_should_not_remove_when_id_does_not_exist(db_session):
    """
    Try to remove menu
    """
    restaurant = RestaurantsModel(id='1', name='Cool place')
    db_session.add(restaurant)
    db_session.commit()
    menu = MenusModel(id="12345", name="my first menu", description="The best first menu", restaurant_id="1")
    db_session.add(menu)
    db_session.commit()

    data = remove_menu(db_session, '45')
    assert data.status == 404
    assert data.content == {'message': 'unable to delete menu 45'}
