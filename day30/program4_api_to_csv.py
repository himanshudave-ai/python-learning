import csv
import json

# Read data from JSON file
with open("users_data.json", "r") as file:
    users = json.load(file)

# Write selected data into CSV
with open("users_data.csv", "w", newline="") as file:
    fieldnames = ["id", "name", "email", "city"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for user in users:
        writer.writerow({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"]
        })

print("CSV FILE CREATED SUCCESSFULLY")
print("------------------------------")
print("Total records exported:", len(users))
print("File created: users_data.csv")