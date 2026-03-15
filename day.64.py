# request module 
# get requests
import requests
response = requests.get("https://www.google.com/")
print(response.text)

# post request
url = "https://jsonplaceholder.typicode.com/posts"
data ={
    "title":'taxi',
    "body":"Bro",
    "userid":120,
  }
headers ={
    'content-type':'application\json ; charset = UTF-8'
  }
respone = requests.post(url,headers=headers,json=data)
print(respone.text)