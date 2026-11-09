import json
import csv
from datetime import datetime
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

URL = "https://jsonplaceholder.typicode.com/users"

def fetch_users():
    with urlopen(URL, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))

def save_json(users):
    with open("automation_users.json", "w") as file:
        json.dump(users, file, indent=4)

def save_csv(users):
    with open("automation_users.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Email", "City"])

        for user in users:
            writer.writerow([
                user["id"],
                user["name"],
                user["email"],
                user["address"]["city"]
            ])

def generate_report(users):
    report = (
        "API AUTOMATION REPORT\n"
        "---------------------\n"
        f"Total Users: {len(users)}\n"
        f"Report Date: {datetime.now():%Y-%m-%d %H:%M:%S}\n"
        "JSON File: automation_users.json\n"
        "CSV File: automation_users.csv\n"
    )

    with open("automation_report.txt", "w") as file:
        file.write(report)

    print(report)

try:
    users = fetch_users()

    save_json(users)
    save_csv(users)
    generate_report(users)

    print("Automation completed successfully!")

except (HTTPError, URLError, TimeoutError) as error:
    print("API request failed:", error)

except (json.JSONDecodeError, KeyError, TypeError) as error:
    print("Data processing failed:", error)

except OSError as error:
    print("File operation failed:", error)