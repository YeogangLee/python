import requests
from bs4 import BeautifulSoup

URL = 'https://vip.mk.co.kr/newSt/rate/item_all.php' 

soup = BeautifulSoup(requests.get(URL).content.decode('euc-kr','replace'), 'lxml')
trs = soup.find_all("td", "st2")

for idx, tr in enumerate(trs) :
    print(tr.next_element.text) # c_name
    print(tr.next_element.attrs['title'])
    print(tr.find_next_sibling().text) # price
    print()
