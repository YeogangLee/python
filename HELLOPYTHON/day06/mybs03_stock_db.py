import requests
import mariadb
import time
from bs4 import BeautifulSoup

conn = mariadb.connect(
    user="root",
    password="python",
    host="localhost",
    database="mypydb")
cur = conn.cursor() 

URL = 'https://vip.mk.co.kr/newSt/rate/item_all.php' 


soup = BeautifulSoup(requests.get(URL).content.decode('euc-kr','replace'), 'lxml')
trs = soup.find_all("td", "st2")
stock_time = soup.find("span", id="mystockThisTimevalue")
date = time.strftime('%Y', time.localtime(time.time())) + stock_time.text[:11].replace(".","").replace(" ","")

'''
print(date)
for idx, tr in enumerate(trs) :
    print(tr.next_element.text) # c_name
    print(tr.next_element.attrs['title'])
    print(tr.find_next_sibling().text) # price
    print()
'''

# insert information 
for idx, tr in enumerate(trs) :
    try: 
        sql = "INSERT INTO stock (s_code, c_name, price, crw_date) VALUES (%s, %s, %d, %s)"
        val = (tr.next_element.attrs['title'], tr.next_element.text, int(tr.find_next_sibling().text.replace(",","")), date)
        cur.execute(sql, val)
         
    except mariadb.Error as e: 
        print(f"Error: {e}")
    
conn.commit()

# retrieve information
cur.execute("SELECT * FROM stock")

print(f"s_code\tc_name\tprice\tcrw_date")
print(f"---------------------")
for s_code, c_name, price, crw_date in cur: 
    print(f"{s_code}\t{c_name}\t\t{price}\t{crw_date}")

conn.close()