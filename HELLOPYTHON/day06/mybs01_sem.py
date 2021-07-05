import requests 
from bs4 import BeautifulSoup

URL = 'http://localhost:8090/HELLOWEB2/hello.jsp' 
response = requests.get(URL)
html = response.text 

soup = BeautifulSoup(html, 'html.parser')
tds = soup.select("td")

# for td in tds :
#    print(td)

# 2 이상부터 td 출력    
for idx, td in enumerate(tds) :
    if idx > 2 :
        # 전부 사용 가능
        # print(td.get_text())
        if idx % 3 == 0 :
            print()
        print(td.text)
        # print(td.string)
        
