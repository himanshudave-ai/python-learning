import json
from urllib.request import urlopen

url = "https://jsonplaceholder.typicode.com/users"

with urlopen(url) as response:
    users = json.loads(response.read().decode("utf-8"))

print("FILTERED USERS")
print("----------------")

for user in users:
    if user["id"] <= 5:
        print("ID:", user["id"])
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("----------------")