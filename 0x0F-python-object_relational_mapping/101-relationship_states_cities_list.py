#!/usr/bin/python3
"""
Write a script that lists all State objects and corresponding City objects
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

    output = session.query(State).order_by(State.id).all()

    for Sts in output:
        print("{}: {}".format(Sts.id, Sts.name))
        for Cts in Sts.cities:
            print("    {}: {}".format(Cts.id, Cts.name))

    session.close()
