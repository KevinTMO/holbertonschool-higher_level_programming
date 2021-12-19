#!/usr/bin/python3
"""
Creating the connection between the script and our database to
send instruction and receive the information we require
"""


from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    User = argv[1]
    Passwd = argv[2]
    Db = argv[3]
    Host = "localhost"

    Engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                           format(User, Passwd, Host, Db))

    Session = sessionmaker(bind=Engine)
    session = Session()
    output = session.query(State.name, City.id, City.name).filter(
        State.id == City.id).order_by(City.id)

    for queries in output:
        print("{}: ({}) {}".format(queries[0], queries[1], queries[2]))

    session.close()
