#!/usr/bin/python3
"""
script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states\
        WHERE BINARY name = '{}'".format(sys.argv[4]))
    rows = c.fetchall()
    [print(row) for row in rows]
