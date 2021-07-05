import mariadb

conn = mariadb.connect(
    user="root",
    password="python",
    host="localhost",
    database="mypydb")
cur = conn.cursor() 

# retrieve information
cur.execute("SELECT * FROM stock")

print(f"s_code\tc_name\t\tprice\tcrw_date")
print(f"---------------------------------------------------------------")
for s_code, c_name, price, crw_date in cur: 
    print(f"{s_code}\t{c_name}\t\t{price}\t{crw_date}")

conn.close()