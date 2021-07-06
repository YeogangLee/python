import requests
from bs4 import BeautifulSoup
from datetime import datetime

yyyy = datetime.today().strftime("%Y%m%d.%H%M")

URL = 'https://vip.mk.co.kr/newSt/rate/item_all.php' 

response = requests.get(URL)
response.encoding = 'euc-kr'
html = response.text

soup = BeautifulSoup(html, 'lxml')
# tds = soup.find_all("td", "st2")
tds = soup.select(".st2")

for idx, td in enumerate(tds) : 
    c_name = td.select_one("a").text
    s_code = td.select_one("a")["title"]
    price = td.parent.select("td")[1].text.replace(",","")
    print(c_name, s_code, price, yyyy)
