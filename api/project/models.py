from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, ForeignKey


Base = declarative_base()

class ItemsModel(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)
    image = Column(String)
    section = Column(String)
    menu_id = Column(String, ForeignKey("menus.id"))


class MenusModel(Base):
    __tablename__ = "menus"
    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    restaurant_id = Column(String, ForeignKey("restaurants.id"))


class RestaurantsModel(Base):
    __tablename__ = "restaurants"
    id = Column(String, primary_key=True)
    name = Column(String)