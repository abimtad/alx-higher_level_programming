#!/usr/bin/python3

"""
script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()
    
    for cs in q:
        print("{}: ({}) {}".format(cs[1].name, cs[0].id, cs[0].name))
