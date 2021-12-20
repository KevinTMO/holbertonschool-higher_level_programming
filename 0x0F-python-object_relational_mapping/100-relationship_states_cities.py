#!/usr/bin/python3
"""
Linking State/City with an attribute using "relationship" to create an State
with a city
"""


from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    User = argv[1]
    Passwd = argv[2]
    Db = argv[3]
    Host = "localhost"

    Engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                           format(User, Passwd, Host, Db))

    Base.metadata.create_all(Engine)
    Session = sessionmaker(bind=Engine)
    session = Session()

    newSt = State(name='California')
    newCt = City(name='San Francisco')
    newSt.cities = [newCt]

    session.add(newSt, newCt)
    session.commit()

    session.close()
