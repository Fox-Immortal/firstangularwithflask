import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "user/1")
print(response.json())

response = requests.get(BASE + "user/0")
print(response.json())

response = requests.get(BASE + "club/0")
print(response.json())
