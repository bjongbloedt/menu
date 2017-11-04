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
        'section': typesystem.String
    }


class MenusSchema(typesystem.Object):
    """
    Menu schema
    """
    properties = {
        'id': typesystem.String,
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