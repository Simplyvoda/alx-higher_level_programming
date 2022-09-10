#!/usr/bin/python3
'''
lists all states with a name specified by user input
'''
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(sys.argv[4]))
    staterows = cur.fetchall()
    for row in staterows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()
