#!/usr/bin/python3
"""
Write a script that lists all City objects from the database
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

    output = session.query(City).order_by(City.id).all()

    for Cts in output:
        print("{}: {} -> {}".format(Cts.id, Cts.name, Cts.state.name))

    session.close()
