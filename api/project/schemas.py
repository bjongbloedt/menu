from apistar import typesystem


class Item(typesystem.Object):
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

class Menu(typesystem.Object):
    """
    Menu schema
    """
    properties = {
        'id': typesystem.String,
        'name': typesystem.String,
        'description': typesystem.String
    }