#!/usr/bin/python3
"""
module 0-select_states: filters the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


def sql_filter(username, passwd, database):
    """that lists all states"""
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
        "SELECT * FROM states ORDER BY id ASC"
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


sql_filter(argv[1], argv[2], argv[3])
