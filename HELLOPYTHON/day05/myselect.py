#!/usr/bin/python 
import mariadb 

conn = mariadb.connect(
    user="root",
    password="python",
    host="localhost",
    database="mypydb")
cur = conn.cursor() 

# retrieve information
cur.execute("SELECT * FROM sampk")

print(f"row01\trow02\trow03")
print(f"---------------------")
for row01, row02, row03 in cur: 
    print(f"{row01}\t{row02}\t{row03}")

conn.close()