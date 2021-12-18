#!/usr/bin/python3

import MySQLdb
from sys import argv

cnndb = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='', db='hbtn_0e_0_usa', charset='utf8')

cur = cnndb.cursor();
cur.execute('SELECT * FROM states ORDER BY id ASC')

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
cnndb.close()
