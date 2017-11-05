import typing
import uuid
from project.schemas import MenusSchema, ItemsSchema, AddMenuRequestSchema, RestaurantsSchema, AddRestaurantSchema, UpdateRestaurantSchema
from project.models import ItemsModel, MenusModel, RestaurantsModel
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
    query = session.query(MenusModel).filter(MenusModel.id == menu_id).first()
    if(query is None):
        data = {'message': f'menu with id {menu_id} was not found'}
        return Response(data, status=404)
    return MenusSchema(query)

def get_menus(session: Session) -> MenusSchema:
    """
    Gets a specific menu by id
    """
    query = session.query(MenusModel).all()
    if(len(query) == 0):
        data = {'message': 'no menus were found'}
        return Response(data, status=404)
    return [MenusSchema(i) for i in query]

def get_items_for_menu(session: Session, menu_id: str) -> typing.List[ItemsSchema]:
    """
    Gets all of the items for the given menu_id
    """
    query = session.query(ItemsModel).filter(ItemsModel.menu_id == menu_id).all()
    if(len(query) == 0):
        data = {'message': f'items for the menu with id {menu_id} were not found'}
        return Response(data, status=404)
    return [ItemsSchema(i) for i in query]

def add_menu_to_restaurant(session: Session, rest_id: str, menu_request: AddMenuRequestSchema) -> MenusSchema:
    """
    Adds a new menu
    """
    if not menu_request:
        data = {'message': 'menu request invalid'}
        return Response(data, status=400)

    menu = MenusModel(id=str(uuid.uuid4()), name=menu_request['name'], description=menu_request['description'], restaurant_id=rest_id)
    session.add(menu)
    session.commit()
    return Response(MenusSchema(id=menu.id, name=menu.name, description=menu.description, restaurant_id=menu.restaurant_id), status=201)

def get_restaurant_by_id(session: Session, restaurant_id: str) -> RestaurantsSchema:
    """
    Gets a specific restaurant by id
    """
    query = session.query(RestaurantsModel).filter(RestaurantsModel.id == restaurant_id).first()
    if(query is None):
        data = {'message': f'restaurant with id {restaurant_id} was not found'}
        return Response(data, status=404)
    return RestaurantsSchema(query)

def add_restaurant(session: Session, restaurant_request: AddRestaurantSchema) -> RestaurantsSchema:
    """
    Adds a new Restuarant
    """
    if not restaurant_request:
        data = {'message': 'restaurant request invalid'}
        return Response(data, status=400)

    restaurant = RestaurantsModel(id=str(uuid.uuid4()), name=restaurant_request['name'])
    session.add(restaurant)
    session.commit()
    return Response(RestaurantsSchema(id=restaurant.id, name=restaurant.name), status=201)

def get_restaurants(session: Session) -> typing.List[RestaurantsSchema]:
    """
    Gets a list of restaurants
    """
    query = session.query(RestaurantsModel).all()
    if(len(query) == 0):
        data = {'message': 'no restaurants were found'}
        return Response(data, status=404)
    return [RestaurantsSchema(i) for i in query]

def update_restaurant_name(session: Session, restaurant_id: str, update_request: UpdateRestaurantSchema) -> RestaurantsSchema:
    """
    update the name of the restaurant
    """
    if(len(update_request['name']) <= 0):
        data = {'message': f'unable to update restaurant {restaurant_id} with name {update_request["name"]}'}
        return Response(data, status=400)
    update = session.query(RestaurantsModel) \
        .filter(RestaurantsModel.id==restaurant_id) \
        .update({'name': update_request['name']})
    session.commit()
    if(update < 1):
        data = {'message': f'unable to update restaurant {restaurant_id} with name {update_request["name"]}'}
        return Response(data, status=404)
    return Response(RestaurantsSchema(id=restaurant_id, name=update_request['name']), status=200)

def remove_restaurant(session: Session, restaurant_id: str):
    """
    remove a restaurant
    """
    if(len(restaurant_id) <= 0):
        data = {'message': f'must provide id'}
        return Response(data, status=400)
    update = session.query(RestaurantsModel) \
        .filter(RestaurantsModel.id==restaurant_id) \
        .delete()
    if(update < 1):
        data = {'message': f'unable to delete restaurant {restaurant_id}'}
        return Response(data, status=404)
    return Response({}, status=204)