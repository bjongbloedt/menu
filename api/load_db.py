#!/user/bin/python
import uuid
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project.models import Base
from project.models import Menus, Items

test_engine = create_engine(os.environ['DATABASE_URL'])
Base.metadata.create_all(test_engine)
Session = sessionmaker(bind=test_engine)
session = Session()

restaurant = RestaurantsModel(id=str(uuid.uuid4()), name='Cool place')
db_session.add(restaurant)
db_session.commit()

menu_one = Menus(id=str(uuid.uuid4()), name="A great menu", description="A great menu", restaurant_id=restaurant.id)
session.add(menu_one)
session.commit()

session.add_all([
    Items(id=str(uuid.uuid4()), name="sandwich one", price=9.99, image="http://image.com/image", section="sandwiches", menu_id=menu_one.id),
    Items(id=str(uuid.uuid4()), name="sandwich two", price=11.99, image="http://image.com/image", section="sandwiches", menu_id=menu_one.id),
    Items(id=str(uuid.uuid4()), name="sandwich three", price=10.99, image="http://image.com/image", section="sandwiches", menu_id=menu_one.id),
    Items(id=str(uuid.uuid4()), name="sandwich four", price=8.99, image="http://image.com/image", section="sandwiches", menu_id=menu_one.id),
    Items(id=str(uuid.uuid4()), name="sandwich five", price=9.99, image="http://image.com/image", section="sandwiches", menu_id=menu_one.id),
    Items(id=str(uuid.uuid4()), name="sandwich six", price=9.99, image="http://image.com/image", section="sandwiches", menu_id=menu_one.id),
    Items(id=str(uuid.uuid4()), name="cake", price=1.99, image="http://image.com/image", section="dessert", menu_id=menu_one.id),
    Items(id=str(uuid.uuid4()), name="cookie", price=1.99, image="http://image.com/image", section="dessert", menu_id=menu_one.id),
    Items(id=str(uuid.uuid4()), name="lemonaid", price=0.99, image="http://image.com/image", section="drink", menu_id=menu_one.id),
    Items(id=str(uuid.uuid4()), name="root beer", price=0.99, image="http://image.com/image", section="drink", menu_id=menu_one.id),
    Items(id=str(uuid.uuid4()), name="soda", price=0.99, image="http://image.com/image", section="drink", menu_id=menu_one.id)
])
session.commit()
session.close()
test_engine.dispose()