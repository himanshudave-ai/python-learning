import csv
import json
from urllib.request import urlopen

url = "https://jsonplaceholder.typicode.com/users"

with urlopen(url) as response:
    users = json.loads(response.read().decode("utf-8"))

with open("users_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Email", "City"])

    for user in users:
        writer.writerow([
            user["id"],
            user["name"],
            user["email"],
            user["address"]["city"]
        ])

print("CSV file created successfully!")
print("Total records:", len(users))