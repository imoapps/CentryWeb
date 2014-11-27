import sqlite3
conn = sqlite3.connect("J:\incomming.db")
if conn :
    print'Connected to Database at {}'.format(conn)
else:
    print '{}'.format(conn.DatabaseError)
conn.close()
