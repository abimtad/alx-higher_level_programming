#!/usr/bin/python3

"""
script that takes in the name of a state as an
argument and lists all cities of that state, using
the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT c.name\
        FROM cities AS c\
            INNER JOIN states AS s\
                ON c.state_id = s.id\
                WHERE s.name = %s\
                    ORDER BY c.id", (sys.argv[4], ))
    rows = c.fetchall()

    for i in range(len(rows)):
        print(rows[i][0], end=", " if i + 1 < len(rows) else "")
    print("")
