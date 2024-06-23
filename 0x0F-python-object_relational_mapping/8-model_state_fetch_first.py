#!/usr/bin/python3
"""Lists the first state object from a database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State.id, State.name).order_by(State.id).first()

    if row:
        print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")
