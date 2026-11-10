import json
from urllib.request import urlopen

users_url = "https://jsonplaceholder.typicode.com/users"
posts_url = "https://jsonplaceholder.typicode.com/posts"

with urlopen(users_url) as response:
    users = json.loads(response.read().decode("utf-8"))

with urlopen(posts_url) as response:
    posts = json.loads(response.read().decode("utf-8"))

print("API DATA FETCHED SUCCESSFULLY")
print("-----------------------------")

print("Total Users:", len(users))
print("Total Posts:", len(posts))

print("\nFIRST 3 USERS")

for user in users[:3]:
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("----------------")