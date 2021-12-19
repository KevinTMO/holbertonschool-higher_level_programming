#!/usr/bin/python3
"""
Insert a new value name for the table states in the field name
And print the id of that new value
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

    newSt = State(name="Louisiana")
    session.add(newSt)
    session.commit()

    print("{}".format(newSt.id))

    session.close()
