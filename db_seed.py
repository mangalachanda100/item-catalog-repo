from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///catalogapp.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

categories = [
    ['Soccer',
        [{'name': 'Soccer Cleats',
          'description': 'Description of Soccer Cleats'},
         {'name': 'Jersey',
          'description': 'Description of Jersey'},
         {'name': 'Two shinguards',
          'description': 'Description of Two shinguards'},
         {'name': 'Shinguards',
          'description': 'Description of Shinguards'}]],
    ['hockey',
        [{'name': 'Stick',
          'description': 'Description of hockey stick'}]],
    ['snowboarding',
        [{'name': 'Goggles',
          'description': 'Description of Goggles'},
         {'name': 'Snowboard',
          'description': 'Description of Snowboard'}]],
    ['frisbee',
        [{'name': 'Frisbee',
          'description': 'Description of Frisbee'}]],
    ['baseball',
        [{'name': 'Bat',
          'description': 'Description of Bat'}]]
]

current_user = User(name="System User", email="system@test.com")
session.add(current_user)
session.commit()

for category in categories:
    current_category = Category(name=category[0], user=current_user)
    session.add(current_category)
    session.commit()

    for item in category[1]:
        current_item = Item(name=item['name'],
                            description=item['description'],
                            category=current_category,
                            user=current_user)
        session.add(current_item)
        session.commit()

print ("Database seeding complete!")
