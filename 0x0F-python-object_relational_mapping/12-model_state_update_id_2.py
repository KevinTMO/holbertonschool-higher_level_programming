#!/usr/bin/python3
"""
Update a state name
"""


from sys import argv
from model_state import State, Base
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

    uptSt = session.query(State).get(2)
    uptSt.name = "New Mexico"
    session.commit()

    session.close()
