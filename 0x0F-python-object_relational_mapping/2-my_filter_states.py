#!/usr/bin/python3
"""
Display only those entires from the state given
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
    cur.execute('SELECT * FROM states WHERE name LIKE "{}%" ORDER BY id ASC'.
                format(argv[4]))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    cnndb.close()
