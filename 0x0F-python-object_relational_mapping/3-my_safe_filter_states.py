#!/usr/bin/python3
"""
module 3-my_safe_filter_states: eliminates sql injection
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost",
        port=3360,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s;", (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
