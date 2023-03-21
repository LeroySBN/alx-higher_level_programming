#!/usr/bin/python3
"""
module 2-my_filter_states
"""
import MySQLdb
from sys import argv


def sql_filter(username, passwd, database, state):
    """
    displays values in the states table where name matches the state argument
    """
    conn = MySQLdb.connect(
        host="localhost",
        port=3360,
        user=username,
        passwd=passwd,
        db=database,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC".format(state)
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


sql_filter(argv[1], argv[2], argv[3], argv[4])
