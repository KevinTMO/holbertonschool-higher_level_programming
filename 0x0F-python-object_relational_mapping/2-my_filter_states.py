#!/usr/bin/python3
"""
Display only those entires from the state given
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    state_arg = argv[4]
    cnndb = MySQLdb.connect(host='localhost',
                            port=3306,
                            user=argv[1],
                            passwd=argv[2],
                            db=argv[3],
                            charset='utf8')

    cur = cnndb.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "{:s}%" ORDER BY id ASC'.
                format(argv[4]))

    for row in cur.fetchall():
        if row[1] == state_arg:
            print(row)

    cur.close()
    cnndb.close()
