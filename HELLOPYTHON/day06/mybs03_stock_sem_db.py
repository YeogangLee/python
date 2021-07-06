import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pymysql
conn = pymysql.connect(user="root", password="python",
                       host="localhost", database="mypydb", charset='utf8')
curs = conn.cursor()

def insertStock(s_code, c_name, price, crw_date):
    sql = "INSERT INTO stock (s_code, c_name, price, crw_date) VALUES (%s, %s, %s, %s)"
    val = (s_code, c_name, price, crw_date)
    curs.execute(sql, val)
    conn.commit()


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
    print(c_name, s_code, price, yyyy)
    insertStock(c_name, s_code, price, yyyy)


conn.close()