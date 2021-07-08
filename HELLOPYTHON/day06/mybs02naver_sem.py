import urllib.request
from bs4 import BeautifulSoup
client_id = "9NUFIPVgF55nN4h1R5i9"
client_secret = "hxzbrMYVAw"
encText = urllib.parse.quote("주식")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText # xml 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    html = response_body.decode('utf-8')
    soup = BeautifulSoup(html, 'xml')
    items = soup.select("item")
    for item in items:
        print(item.title.text,end="\n")
        print(item.originallink.text,end="\n")
        print(item.link.text,end="\n")
        print(item.description.text,end="\n")
        print(item.pubDate.text,end="\n")
        print()
    
else:
    print("Error Code:" + rescode)