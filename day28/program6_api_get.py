import json
from urllib.request import urlopen

url = "https://jsonplaceholder.typicode.com/users/1"

with urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

print("USER DETAILS")
print("------------")
print("Name:", data["name"])
print("Email:", data["email"])
print("City:", data["address"]["city"])
print("Company:", data["company"]["name"])