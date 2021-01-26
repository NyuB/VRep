
#!/bin/python

import pycassa
import sys

pool = pycassa.ConnectionPool(keyspace='mybible', server_list=['127.0.0.1:9160']
)
bible =  pycassa.ColumnFamily(pool, 'bible')

l = 0
for line in sys.stdin:
    print(line)
    bible.insert(l, {'line':line})
    l += 1
