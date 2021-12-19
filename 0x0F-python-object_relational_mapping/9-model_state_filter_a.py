#!/usr/bin/python3
"""
Display only the entires that contains the letter 'a'
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
    output = session.query(State).filter(State.name.like == ('a%')).\
        order_by(State.id)

    for rows in output:
        print("{}: {}".format(rows.id, rows.name))

    session.close()
