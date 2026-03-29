#newsapi 
import requests
import json
query = input("kis chiz ki news jaana chate ho:")
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-02-28&sortBy=publishedAt&apiKey=f9a572adf2a445cd979740652c4607ba"
r = requests.get(url)
news = json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------------------")
