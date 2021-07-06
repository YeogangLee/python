#!/usr/bin/python 
import mariadb 

conn = mariadb.connect(
    user="root",
    password="python",
    host="localhost",
    database="mypydb",
    charset="utf8")

cur = conn.cursor()

def insertStock(s_code, c_name, price, crw_date):
    sql = "INSERT INTO stock (s_code, c_name, price, crw_date) VALUES (%s, %s, %s, %s)"
    val = (s_code, c_name, price, crw_date)
    cur.execute(sql, val)
    conn.commit()
    
insertStock("1","1","1","1")

conn.close()