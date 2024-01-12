from models import Dog
from sqlalchemy.orm import sessionmaker

def create_table(base, engine):
    base.metadata.create_all(engine)
    # Session = sessionmaker(bind=engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name.like(f"%{name}%")).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name.like(f"%{name}%"), Dog.breed.like(f"%{breed}%")).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()