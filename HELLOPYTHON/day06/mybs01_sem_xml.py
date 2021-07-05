import requests 
from bs4 import BeautifulSoup

# URL = 'http://localhost:8090/HELLOWEB2/hello.jsp' 
URL = 'http://localhost:8090/HELLOWEB2/stock.xml' 
response = requests.get(URL)
html = response.text 

# BeautifulSoup(markup, features, builder, parse_only, from_encoding, exclude_encodings, element_classes)
soup = BeautifulSoup(html, 'html.parser')
items = soup.select("item")

for idx, item in enumerate(items) :
    print("item : " + str(idx + 1) + " ----------------------------------------------------")
    text_title = item.title.text.replace("&quot;", "\"").replace("<b>","").replace("</b>","")
    text_title_join = ' '.join(text_title.split())
    text_replace = item.description.text.replace("<b>주식</b>", "")
    text_join = ' '.join(text_replace.split()).replace("다.", "다.\n").replace("&quot;", "\"").replace("<b>","").replace("</b>","").replace("&lt;", "<").replace("&gt;", ">")
    print(text_title_join, end="\n\n")
    print(text_join)
    print()
    print()
    