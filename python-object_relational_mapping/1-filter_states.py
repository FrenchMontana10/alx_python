#!/usr/bin/python3
""" Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    
    # Execute the SQL query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    
    # Fetch and print the results
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Close the cursor and database connection
    cur.close()
    db.close()
