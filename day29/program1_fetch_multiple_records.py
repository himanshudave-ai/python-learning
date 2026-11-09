import json
from urllib.request import urlopen

url = "https://jsonplaceholder.typicode.com/users"

with urlopen(url) as response:
    users = json.loads(response.read().decode("utf-8"))

print("TOTAL USERS:", len(users))
print("-------------------------")

for user in users:
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("City:", user["address"]["city"])
    print("-------------------------")