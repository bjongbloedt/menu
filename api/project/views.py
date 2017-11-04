import typing
from project.schemas import Menu, Item


def ping():
    """
    Healthcheck endpoint
    """
    return {'message': 'ok'}

def get_menu_by_id(menu_id: str) -> typing.List[Menu]:
    """
    Gets a specific menu by id
    """
    return Menu(name="my first menu", id=menu_id, description="The best first menu")

def get_items_for_menu(menu_id: str) -> typing.List[Item]:
    """
    Gets all of the items for the given menu_id
    """
    return [
        Item(id='1', name='A menu item', price=9.99, image='http://google.com', section='dessert')
    ]