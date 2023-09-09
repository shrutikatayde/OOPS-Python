import requests
import json
from bs4 import BeautifulSoup

# POST REQUEST

# url = "https://jsonplaceholder.typicode.com/posts"
#
# data = {"userId": 1, "id": 1, "title": "Shrutika", "body": "developer"}
#
# headers = {
#     "Content-type": "application/json ; charset=UTF-8",
# }
#
#
# response = requests.post(url, headers=headers, json=data)
# print(response.json())

# GET REQUEST

url = "https://www.programiz.com/python-programming/online-compiler2/"

g = requests.get(url)
# print(g.text)

soup = BeautifulSoup(g.text, "html.parser")

print(soup.prettify())
