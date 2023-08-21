#!/usr/bin/python3
""" Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    # Create the database and table if they don't exist
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa")
    cur.execute("USE hbtn_0e_0_usa")
    cur.execute("CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id))")
    
    # Insert some data into the states table
    cur.execute("INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas'), ('New York'), ('Nevada')")
    
    # Execute the SQL query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    
    # Fetch and print the results
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Close the cursor and database connection
    cur.close()
    db.close()
