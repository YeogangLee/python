import requests
from bs4 import BeautifulSoup

URL = 'http://localhost:8090/HELLOWEB2/hello.jsp' 
response = requests.get(URL) 

html = response.text
soup = BeautifulSoup(html, 'html.parser')
all_tds = soup.find_all("td")

j = 0
for i in all_tds :
    print(i.string)
    j+=1
    if(j == 3) :
        print()
        j = 0
