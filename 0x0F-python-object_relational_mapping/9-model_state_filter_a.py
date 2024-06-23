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

    result = session.query(State.id, State.name).\
        filter(State.name.like("%a%")).order_by(State.id).all()

    for row in result:
        print("{}: {}".format(row.id, row.name))
