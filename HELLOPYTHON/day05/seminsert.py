import pymysql

conn = pymysql.connect(
    user="root",
    password="python",
    host="localhost",
    database="mypydb")

cur = conn.cursor() 

# insert information
sql = "INSERT INTO sampk (ROW02, ROW03) VALUES (%s,%s)"
val = ("3", "3")
cur.execute(sql, val)
cnt = cur.rowcount

print("cnt", cnt)


conn.close()