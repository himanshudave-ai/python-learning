import json
import csv
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

url = "https://jsonplaceholder.typicode.com/users"

try:
    with urlopen(url, timeout=10) as response:
        users = json.loads(response.read().decode("utf-8"))

    with open("api_users_report.csv", "w", newline="") as file:
        fields = ["id", "name", "email", "city", "company"]

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for user in users:
            writer.writerow({
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "city": user["address"]["city"],
                "company": user["company"]["name"]
            })

    print("API AUTOMATION COMPLETED")
    print("------------------------")
    print("Total users processed:", len(users))
    print("CSV report generated: api_users_report.csv")

except HTTPError as error:
    print("HTTP Error:", error.code)

except URLError as error:
    print("Connection Error:", error.reason)

except TimeoutError:
    print("Request timed out.")