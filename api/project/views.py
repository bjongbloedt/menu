import typing
import uuid
from project.schemas import MenusSchema, ItemsSchema, AddMenuRequestSchema
from project.models import Items as ItemModel
from project.models import Menus as MenuModel
from apistar.backends.sqlalchemy_backend import Session
from apistar import Response


def ping():
    """
    Healthcheck endpoint
    """
    return {'message': 'ok'}

def get_menu_by_id(session: Session, menu_id: str) -> MenusSchema:
    """
    Gets a specific menu by id
    """
    query = session.query(MenuModel).filter(MenuModel.id == menu_id).first()
    if(query is None):
        data = {'message': f'menu with id {menu_id} was not found'}
        return Response(data, status=404)
    return MenusSchema(query)

def get_menus(session: Session) -> MenusSchema:
    """
    Gets a specific menu by id
    """
    query = session.query(MenuModel).all()
    if(len(query) == 0):
        data = {'message': 'no menus were found'}
        return Response(data, status=404)
    return [MenusSchema(i) for i in query]

def get_items_for_menu(session: Session, menu_id: str) -> typing.List[ItemsSchema]:
    """
    Gets all of the items for the given menu_id
    """
    query = session.query(ItemModel).filter(ItemModel.menu_id == menu_id).all()
    if(len(query) == 0):
        data = {'message': f'items for the menu with id {menu_id} were not found'}
        return Response(data, status=404)
    return [ItemsSchema(i) for i in query]

def add_menu(session: Session, menu_request: AddMenuRequestSchema) -> MenusSchema:
    """
    Adds a new menu
    """
    if not menu_request:
        data = {'message': 'menu request invalid'}
        return Response(data, status=400)

    menu = MenuModel(id=str(uuid.uuid4()), name=menu_request['name'], description=menu_request['description'])
    session.add(menu)
    session.commit()
    return Response(MenusSchema(id=menu.id, name=menu.name, description=menu.description), status=201)
