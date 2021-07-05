import requests 
# URL = 'http://www.tistory.com'
URL = 'http://localhost:8090/HELLOWEB2/hello.jsp' 
response = requests.get(URL) 

print(response.status_code)
print(response.text)

# response.status_code 
# response.text
