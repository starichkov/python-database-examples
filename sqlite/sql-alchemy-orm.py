import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Jedi(Base):
    __tablename__ = 'jedi'
    id = sa.Column('id', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.String)
    phone = sa.Column('phone', sa.String)

    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def __repr__(self):
        return "Jedi (#{}) - {}, {}".format(self.id, self.name, self.phone)


connection_string = 'sqlite:///sql-alchemy-orm-jedi-order.db'

connection = sa.create_engine(connection_string)

# create database and table
Base.metadata.create_all(connection)

jedi1 = Jedi(1, 'Qui-Gon Jinn', '777-999-50-50')
jedi2 = Jedi(2, 'Obi-Wan Kenobi', '777-999-51-51')
jedi3 = Jedi(3, 'Anakin Skywalker', '777-999-52-52')

# create session for connection to be able to save our Jedi to theirs table
Session = sessionmaker(bind=connection)
session = Session()

session.add(jedi1)
session.add_all([jedi2, jedi3])

session.commit()

jedi = session.query(Jedi).all()

for single in jedi:
    print(single)
