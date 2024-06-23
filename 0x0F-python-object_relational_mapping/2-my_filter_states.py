#!/usr/bin/python3
"""A script that provides a searched result from a database"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched = sys.argv[4]

    connection = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states\
                   WHERE BINARY name = '{}'\
                   ORDER BY id".format(searched))
    result = cursor.fetchall()

    for row in result:
        print(row)
    cursor.close()
    connection.close()
