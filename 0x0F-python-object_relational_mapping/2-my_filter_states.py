#!/usr/bin/python3
"""
module 2-my_filter_states
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
    cur.execute(
        "SELECT * \
        FROM states \
        WHERE CONVERT(`name` USING Latin1) \
        COLLATE Latin1_General_CS = '{}';"
        .format(argv[4])
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
