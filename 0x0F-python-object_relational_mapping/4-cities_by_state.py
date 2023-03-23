#!/usr/bin/python3
"""
module 4-cities_by_state: lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("\
    SELECT \
    ct.id, ct.name, st.name \
    FROM \
    cities as ct \
    LEFT JOIN states as st \
    ON st.id=ct.state_id;")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
