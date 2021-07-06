import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
import pymysql
conn = pymysql.connect(user="root", password="python",
                       host="localhost", database="mypydb", charset='utf8')
curs = conn.cursor()

def insertStock(s_code, c_name, price, crw_date):
    sql = "INSERT INTO stock (s_code, c_name, price, crw_date) VALUES (%s, %s, %s, %s)"
    val = (s_code, c_name, price, crw_date)
    curs.execute(sql, val)
    conn.commit()


for i in range(6) :
    
    yyyy = datetime.today().strftime("%Y%m%d.%H%M")
    
    URL = 'https://vip.mk.co.kr/newSt/rate/item_all.php' 
    response = requests.get(URL)
    response.encoding = 'euc-kr'
    html = response.text
    
    
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.select(".st2")
    
    
    
    for idx, td in enumerate(tds) :
        c_name = td.select_one("a").text
        s_code = td.select_one("a")["title"]
        price = td.parent.select("td")[1].text.replace(",","")
        print(s_code, c_name, price, yyyy)
        insertStock(s_code, c_name, price, yyyy)
                
    # for j in range(10) : 
        # insertStock(j,i,i,i)
        
    sleep(60)


conn.close()