#!/usr/bin/python3
"""
Look for the id of the state given
If the state doesnt exist then print Not found
"""


from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    User = argv[1]
    Passwd = argv[2]
    Db = argv[3]
    st = argv[4]
    Host = "localhost"

    Engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                           format(User, Passwd, Host, Db))

    Session = sessionmaker(bind=Engine)
    session = Session()
    output = session.query(State).filter_by(name=st).first()

    if output:
        print("{}".format(output.id))
    else:
        print("Not found")

    session.close()
