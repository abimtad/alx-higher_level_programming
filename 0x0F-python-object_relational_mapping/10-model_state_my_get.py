#!/usr/bin/python3
"""Searches for a state object from a database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    state_name = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.id, State.name).\
        filter(State.name.like(state_name)).order_by(State.id).one_or_none()

    if result:
        print(result.id)
    else:
        print("Not found")
