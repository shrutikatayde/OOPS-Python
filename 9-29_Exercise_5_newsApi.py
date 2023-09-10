import requests
import json

query = input("Which type of news yo want to read today ?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-08-10&sortBy=publishedAt&apiKey= drop here your api key"
news = requests.get(url)
res_in_json = json.loads(news.text)
# print(res_in_json, type(res_in_json))

for article in res_in_json["articles"]:
    print("Headline: ", article["title"])
    print("Description: ", article["description"])
