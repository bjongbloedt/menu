import typing
from project.schemas import Menu as MenuSchema
from project.schemas import Item as ItemSchema
from project.models import Items as ItemModel
from project.models import Menus as MenuModel
from apistar.backends.sqlalchemy_backend import Session
from apistar import Response


def ping():
    """
    Healthcheck endpoint
    """
    return {'message': 'ok'}

def get_menu_by_id(session: Session, menu_id: str) -> MenuSchema:
    """
    Gets a specific menu by id
    """
    query = session.query(MenuModel).filter(MenuModel.id == menu_id).first()
    if(query is None):
        data = {'message': f'menu with id {menu_id} was not found'}
        return Response(data, status=404)
    return MenuSchema(query)

def get_items_for_menu(session: Session, menu_id: str) -> typing.List[ItemSchema]:
    """
    Gets all of the items for the given menu_id
    """
    query = session.query(ItemModel).filter(ItemModel.menu_id == menu_id).all()
    if(len(query) == 0):
        data = {'message': f'items for the menu with id {menu_id} were not found'}
        return Response(data, status=404)
    return [ItemSchema(i) for i in query]
