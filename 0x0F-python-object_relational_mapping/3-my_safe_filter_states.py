#!/usr/bin/python3

import MySQLdb
from sys import argv

state_name = argv[4]

cnndb = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset='utf8')

cur = cnndb.cursor()
cur.execute('SELECT * FROM states WHERE name = %(state_name)s ORDER BY id ASC', {'state_name': state_name})

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
cnndb.close()
