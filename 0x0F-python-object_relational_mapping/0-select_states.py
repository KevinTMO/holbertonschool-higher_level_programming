#!/usr/bin/python3

import MySQLdb

cnndb = MySQLdb.connect(host='localhost', user='root', passwd='', db='hbtn_0e_0_usa', charset='utf8')

cur = cnndb.cursor();
cur.execute('SELECT * FROM states ORDER BY id ASC')

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
cnndb.close()
