#!/usr/bin/python3
"""
Write a script that filter ocurrences of cities in states by id
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    cnndb = MySQLdb.connect(host='localhost',
                            port=3306,
                            user=argv[1],
                            passwd=argv[2],
                            db=argv[3],
                            charset='utf8')

    cur = cnndb.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name FROM cities,\
    states WHERE states.id = state_id')

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    cnndb.close()
