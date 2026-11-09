import json
from urllib.request import urlopen

url = "https://jsonplaceholder.typicode.com/users"

with urlopen(url) as response:
    users = json.loads(response.read().decode("utf-8"))

with open("users_data.json", "w") as file:
    json.dump(users, file, indent=4)

print("API data saved successfully!")
print("Total records saved:", len(users))
print("File created: users_data.json")