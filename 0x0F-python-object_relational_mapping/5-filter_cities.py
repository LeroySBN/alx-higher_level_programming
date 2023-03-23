#!/usr/bin/python3
"""
module 4-filter_cities:
lists all cities of state, using the database hbtn_0e_4_usa
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
    ct.name \
    FROM \
    cities as ct LEFT JOIN states as st ON st.id=ct.state_id \
    WHERE \
    st.name = %s;", (argv[4],))
    states = cur.fetchall()
    print(", ".join([state[0] for state in states]))
    cur.close()
    conn.close()
