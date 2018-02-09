from apistar import typesystem


class ItemsSchema(typesystem.Object):
    """
    Menu item schema
    """
    properties = {
        'id': typesystem.String,
        'name': typesystem.String,
        'price': typesystem.Number,
        'image': typesystem.String,
        'section': typesystem.String,
        'menu_id': typesystem.String
    }


class AddItemRequestSchema(typesystem.Object):
    """
    Menu item schema
    """
    properties = {
        'name': typesystem.String,
        'price': typesystem.Number,
        'image': typesystem.String,
        'section': typesystem.String
    }


class MenusSchema(typesystem.Object):
    """
    Menu schema
    """
    properties = {
        'id': typesystem.String,
        'name': typesystem.String,
        'description': typesystem.String,
        'restaurant_id': typesystem.String
    }


class UpdateMenusSchema(typesystem.Object):
    """
    Request to update Menu
    """
    properties = {
        'name': typesystem.String,
        'description': typesystem.String
    }


class AddMenuRequestSchema(typesystem.Object):
    """
    Request to add new menu
    """
    properties = {
        'name': typesystem.String,
        'description': typesystem.String
    }


class RestaurantsSchema(typesystem.Object):
    """
    Restaurant Schema
    """
    properties = {
        'id': typesystem.String,
        'name': typesystem.String
    }


class AddRestaurantSchema(typesystem.Object):
    """
    Request to add new restaurant
    """
    properties = {
        'name': typesystem.String
    }


class UpdateRestaurantSchema(typesystem.Object):
    """
    Request to update a restaurant
    """
    properties = {
        'name': typesystem.String
    }
