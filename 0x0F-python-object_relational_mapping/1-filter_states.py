#!/usr/bin/python3
"""
Lists all states with name starting by N (uppercase)
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
    cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC')

    rows = cur.fetchall()

    for row in rows:
        if row[1][0]:
            print(row)

    cur.close()
    cnndb.close()
