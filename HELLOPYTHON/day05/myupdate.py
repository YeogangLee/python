#!/usr/bin/python 
import mariadb 

conn = mariadb.connect(
    user="root",
    password="python",
    host="localhost",
    database="mypydb")
cur = conn.cursor() 

# update information 
try: 
    cur.execute("UPDATE sampk SET ROW02 = '4', ROW03 = '4' WHERE ROW01 > 2") 
except mariadb.Error as e: 
    print(f"Error: {e}")
    
conn.commit()


# 확인
cur.execute("SELECT * FROM sampk")

print(f"row01\trow02\trow03")
print(f"---------------------")
for row01, row02, row03 in cur: 
    print(f"{row01}\t{row02}\t{row03}")

conn.close()