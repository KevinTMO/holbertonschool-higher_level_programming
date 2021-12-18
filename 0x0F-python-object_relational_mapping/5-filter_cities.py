#!/usr/bin/python3

import MySQLdb
from sys import argv

state_name = argv[4]

cnndb = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset='utf8')

cur = cnndb.cursor()
cur.execute('SELECT cities.name FROM cities, states WHERE states.name = %(state_name)s AND state_id = states.id',{'state_name': state_name})

rows = cur.fetchall()
cities = ()

for row in rows:
    cities += row
print(', '.join(cities))

cur.close()
cnndb.close()
