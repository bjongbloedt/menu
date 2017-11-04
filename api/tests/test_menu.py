import json
from project.views import get_items_for_menu, get_menu_by_id, ping, get_menus, add_menu
from project.models import Menus as MenuModel
from project.models import Items as ItemModel
from project.schemas import MenusSchema, ItemsSchema, AddMenuRequestSchema


def test_ping():
    """
    Test ping
    """
    data = ping()
    assert data == {'message': 'ok'}


def test_get_menu_by_id(db_session):
    """
    Test getting a single menu
    """
    menu = MenuModel(id="1", name="my first menu", description="The best first menu")
    db_session.add(menu)
    db_session.commit()

    data = get_menu_by_id(db_session, '1')
    assert data == {'id': '1', 'name': 'my first menu',
                    'description': 'The best first menu'}

def test_get_menu_by_id_should_return_error(db_session):
    """
    Test getting a single menu
    """
    data = get_menu_by_id(db_session, '1234123')
    assert data.content ==\
        {'message': 'menu with id 1234123 was not found'}


def test_get_items_for_menu_should_return_items_on_menu(db_session):
    """
    Test getting all items for a menu
    """
    menu = MenuModel(id="2", name="my first menu", description="The best first menu")
    db_session.add(menu)
    db_session.commit()
    item = ItemModel(id="1", name='A menu item', price=9.99, image="http://google.com", section="dessert", menu_id="2")
    db_session.add(item)
    db_session.commit()
    itemtwo = ItemModel(id="3", name='A menu item', price=9.99, image="http://google.com", section="dessert", menu_id="3")
    db_session.add(itemtwo)
    db_session.commit()

    data = get_items_for_menu(db_session, '2')
    assert data ==\
        [{'id': '1', 'name': 'A menu item', 'price': 9.99,
          'image': 'http://google.com', 'section': 'dessert'}]

def test_get_items_for_menu_should_return_error_if_menu_is_not_found(db_session):
    """
    Test getting all items for a menu
    """
    menu = MenuModel(id="2", name="my first menu", description="The best first menu")
    db_session.add(menu)
    db_session.commit()
    item = ItemModel(id="1", name='A menu item', price=9.99, image="http://google.com", section="dessert", menu_id="2")
    db_session.add(item)
    db_session.commit()
    itemtwo = ItemModel(id="3", name='A menu item', price=9.99, image="http://google.com", section="dessert", menu_id="3")
    db_session.add(itemtwo)
    db_session.commit()

    data = get_items_for_menu(db_session, '50')
    assert data.content ==\
        {'message': 'items for the menu with id 50 were not found'}

def test_get_items_for_menu_should_return_empty_list_if_no_items_match_menu_id(db_session):
    """
    Test getting all items for a menu
    """
    menu = MenuModel(id="12345", name="my first menu", description="The best first menu")
    db_session.add(menu)
    db_session.commit()
    item = ItemModel(id="1", name='A menu item', price=9.99, image="http://google.com", section="dessert", menu_id="3")
    db_session.add(item)
    db_session.commit()
    itemtwo = ItemModel(id="3", name='A menu item', price=9.99, image="http://google.com", section="dessert", menu_id="3")
    db_session.add(itemtwo)
    db_session.commit()

    data = get_items_for_menu(db_session, '12345')
    assert data.content ==\
        {'message': 'items for the menu with id 12345 were not found'}


def test_get_menus_should_return_all_menus(db_session):
    """
    Test that all menus are returned
    """
    db_session.add_all([
        MenuModel(id="12345", name="my first menu", description="The best first menu"),
        MenuModel(id="54321", name="my first menu", description="The best first menu")
    ])
    db_session.commit()

    data = get_menus(db_session)
    assert len(data) == 2


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
    data = add_menu(db_session, {'name': 'new menu', 'description': 'A new menu'})
    assert data.status == 201
    assert data.content['name'] == 'new menu'
    assert data.content['description'] == 'A new menu'

    query = db_session.query(MenuModel).filter(MenuModel.id == data.content['id']).first()
    assert query is not None


def test_add_new_menu_should_return_invalid_when_request_is_incorrect(db_session):
    """
    Test that a new menu can be added
    """
    data = add_menu(db_session, {})
    assert data.status == 400
    print(data.content)
    assert data.content == {'message': 'menu request invalid'}